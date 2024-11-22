import os
from concurrent.futures import ThreadPoolExecutor

# Caminho completo para o arquivo de log
LOG_FILE = r"C:\Users\User\Desktop\SO\access.log"

def process_log_lines(lines):
    """
    Processa um intervalo de linhas do log e calcula:
    - A contagem de acessos por hora.
    - O número total de respostas com status 200.
    """
    hourly_access_count = {}
    status_200_count = 0

    try:
        for line in lines:
            parts = line.split()
            if len(parts) > 8:
                timestamp = parts[3][1:]  # Remove o colchete inicial
                status_code = parts[8]

                # Extrai a hora do timestamp
                date_parts = timestamp.split(':')
                if len(date_parts) > 1:
                    hour = date_parts[1]

                    # Incrementa a contagem de acessos para a hora
                    hourly_access_count[hour] = hourly_access_count.get(hour, 0) + 1

                    # Incrementa a contagem de status 200
                    if status_code == '200':
                        status_200_count += 1
    except Exception as e:
        print(f"Erro ao processar linhas do log: {e}")

    return hourly_access_count, status_200_count


def process_log_file(log_file, num_threads=4):
    """
    Lê o arquivo de log e processa em múltiplos threads.
    """
    try:
        if not os.path.isfile(log_file):
            raise FileNotFoundError(f"Arquivo de log não encontrado: {log_file}")

        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        chunk_size = len(lines) // num_threads
        line_chunks = [
            lines[i * chunk_size : len(lines) if i == num_threads - 1 else (i + 1) * chunk_size]
            for i in range(num_threads)
        ]

        combined_hourly_access_count = {}
        total_status_200_count = 0

        # Usa ThreadPoolExecutor para lidar com threads
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            try:
                results = executor.map(process_log_lines, line_chunks)
            except Exception as e:
                print(f"Erro ao executar threads: {e}")
                return {}, 0

        for hourly_access_count, status_200_count in results:
            total_status_200_count += status_200_count
            for hour, count in hourly_access_count.items():
                combined_hourly_access_count[hour] = combined_hourly_access_count.get(hour, 0) + count

        return combined_hourly_access_count, total_status_200_count

    except FileNotFoundError as e:
        print(e)
    except PermissionError:
        print(f"Permissão negada para acessar o arquivo: {log_file}")
    except Exception as e:
        print(f"Erro inesperado ao processar o arquivo de log: {e}")

    # Retorna valores padrão em caso de erro
    return {}, 0


if __name__ == "__main__":
    try:
        # Verifica se o arquivo de log existe
        if not os.path.exists(LOG_FILE):
            raise FileNotFoundError(f"Arquivo de log não encontrado: {LOG_FILE}")

        hourly_access_count, total_status_200_count = process_log_file(LOG_FILE)

        # Exibe os resultados
        print("Acessos por hora:", hourly_access_count)
        print("Total de respostas com código 200:", total_status_200_count)

    except Exception as e:
        print(f"Erro fatal: {e}")

