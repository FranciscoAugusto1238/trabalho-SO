# Análise de Log de Servidor Web com Multithreading em Python

## Visão Geral

Este projeto apresenta uma solução multithreaded para análise de arquivos de log de servidores web. A aplicação foi desenvolvida para processar grandes volumes de dados de forma eficiente, gerando estatísticas diárias importantes, como o número de acessos por hora e a quantidade de respostas bem-sucedidas (código de status 200).

## Contexto

**Atividade Avaliativa: Análise de Log de Servidor Web**

Uma empresa de tecnologia gerencia diversos servidores web que geram grandes arquivos de log diariamente. Esses logs contêm informações cruciais, como endereços IP dos usuários, datas de acesso e códigos de status das respostas. A empresa necessita processar esses logs para gerar estatísticas diárias que auxiliem na monitoração do desempenho do sistema, identificação de padrões de uso e detecção de possíveis problemas.

## Funcionalidades

- **Processamento Multithreaded**: Utiliza múltiplas threads para dividir e processar o arquivo de log, aumentando a eficiência e reduzindo o tempo de execução.
- **Contagem de Acessos por Hora**: Calcula o número de acessos ao servidor para cada hora do dia.
- **Contagem de Respostas com Código 200**: Determina a quantidade total de respostas HTTP com o código de status 200, indicando sucesso.
- **Tratamento de Erros**: Implementa robustos mecanismos de tratamento de erros para garantir a estabilidade da aplicação.
- **Relatórios de Resultados**: Exibe estatísticas geradas de forma clara e organizada.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.13.0
- **Bibliotecas**:
  - `os`
  - `concurrent.futures`
  - `threading`

## Requisitos

- **Python**: Versão 3.13.0
- **Sistema Operacional**: Windows (AMD64)

## Instalação

1. **Clone o Repositório**
    ```bash
    git clone https://github.com/seu-usuario/analise-log-web.git
    ```
2. **Navegue para o Diretório do Projeto**
    ```bash
    cd analise-log-web
    ```
3. **Instale as Dependências**
    Este projeto utiliza apenas bibliotecas padrão do Python, portanto, não há dependências externas a serem instaladas.

## Uso

1. **Configure o Caminho do Arquivo de Log**
   
   Edite a variável `LOG_FILE` no script principal para apontar para o arquivo de log que deseja analisar.
   ```python
   LOG_FILE = r"C:\Users\User\Desktop\SO\access.log"
