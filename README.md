# FederalReserveWebscraping
Desafio técnico de webscraping. Selenium + Python + BeautifulSoup.

Este script Python automatiza a extração de dados CNPJ do site da Receita Federal usando Selenium e BeautifulSoup.

## Pré-requisitos

- Python 3.x
- Navegador Google Chrome
- Chromedriver
- Arquivo CSV de entrada chamado `input.csv`

## Instalação

1. Clone este repositório:

    git clone https://github.com/your-username/cnpj-web-scraping.git
    cd cnpj-web-scraping```

2. pip install undetected-chromedriver selenium beautifulsoup4 pandas

### Uso
  Adicionar CNPJs a input.csv.
  Rodar o código com o python3.
  Preencher o captcha.
  Aguardar.
  Preencher o captcha.
  Por fim, conferir o arquivo output.csv.

### Detalhes do script
  - NÃO resolve o desafio hCaptcha.
  - Insere CNPJ, extrai dados e salva em CSV.
  - Lida com casos em que nenhum dado é encontrado.