# DesafioETL-TOTVS

# Projeto ETL com Python

## Sobre o projeto
Este projeto foi desenvolvido com o objetivo de aplicar na prática o conceito de ETL (Extração, Transformação e Carregamento), utilizando Python e arquivos CSV.

Como a API proposta no desafio pode ficar indisponível, foi utilizada uma abordagem alternativa com dados locais em CSV, garantindo a execução completa do fluxo.

## Etapas do ETL

### 1. Extração
Os dados dos clientes são lidos a partir do arquivo `dados_clientes.csv`.

### 2. Transformação
O sistema analisa as informações dos clientes e gera mensagens personalizadas com base no limite disponível.

### 3. Carregamento
Os dados transformados são salvos no arquivo `mensagens_geradas.csv`.

## Tecnologias utilizadas
- Python
- CSV
- Lógica de programação

## Como executar
1. Certifique-se de ter o Python instalado.
2. Coloque os arquivos na mesma pasta.
3. Execute no terminal:

```bash
python main.py