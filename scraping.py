import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

keys = [
        'cnpj', 'inscricao', 'abertura', 'nome_empresarial', 'titulo_estabelecimento',
        'porte', 'codigo_principal', 'codigo_secundario', 'codigo_juridico',
        'logradouro', 'numero', 'complemento', 'cep', 'bairro', 'municipio',
        'uf', 'endereco_eletronico', 'telefone', 'ente', 'situacao',
        'data_situacao', 'motivo_situacao', 'situacao_especial', 'data_situacao_especial'
    ]

def handleData(xpath):
    info_element = driver.find_element(By.XPATH, xpath)
    info_html = info_element.get_attribute('innerHTML')
    soup = BeautifulSoup(info_html, 'html.parser')
    info = soup.get_text(strip=True)
    return info

def preenche_dict(*args):
    dictt = {k: v for k, v in zip(keys, args)}
    return dictt


def append_to_csv(row_dict):

    with open("output.csv", mode='a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=keys, delimiter=';')

        if csv_file.tell() == 0:
            csv_writer.writeheader()

        csv_writer.writerow(row_dict)

driver = uc.Chrome()

wait = WebDriverWait(driver, 50)
driver.get("https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp")


cnpj_list = pd.read_csv('./input.csv')

for cnpj_code in cnpj_list['CNPJs']:
    print(cnpj_code)
    
    # muda pro frame do captcha
    frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe[title="Widget contendo caixa de seleção para desafio de segurança hCaptcha"]')))
    driver.switch_to.frame(frame)

    # espera o box de captcha estar filled
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-checked="true"]')))

    # volta pro frame comum
    driver.switch_to.default_content()

    # encontra o input de cnpj, insere
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#cnpj"))).send_keys(cnpj_code)
    # clica em consultar
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()

    try:
        l= driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
        print("não achou")
        row_dict = preenche_dict(cnpj_code)
        print(row_dict)
        append_to_csv(row_dict)
        driver.get("https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp")

    except NoSuchElementException:
        # espera a pagina de resultados carregar
        wait.until(EC.presence_of_element_located((By.ID, 'principal')))

        #decidi fazer assim mesmo.
        inscricao = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[2]//tbody//tr//td[1]//font[2]")
        abertura = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[2]//tbody//tr//td[3]//font[2]")
        nome_empresarial = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[3]//tbody//tr//td//font[2]")
        titulo_estabelecimento = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[4]//tbody//tr//td[1]//font[2]")
        porte = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[4]//tbody//tr//td[3]//font[2]")
        codigo_principal = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[5]//tbody//tr//td//font[2]")
        codigo_secundario = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[6]//tbody//tr//td//font[2]")
        codigo_juridico = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[7]//tbody//tr//td//font[2]")
        logradouro = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[8]//tbody//tr//td[1]//font[2]")
        numero = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[8]//tbody//tr//td[3]//font[2]")
        complemento = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[8]//tbody//tr//td[5]//font[2]")
        cep = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[9]//tbody//tr//td[1]//font[2]")
        bairro = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[9]//tbody//tr//td[3]//font[2]")
        municipio = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[9]//tbody//tr//td[5]//font[2]")
        uf = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[9]//tbody//tr//td[7]//font[2]")
        endereco_eletronico = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[10]//tbody//tr//td[1]//font[2]")
        telefone = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[10]//tbody//tr//td[3]//font[2]")
        ente = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[11]//tbody//tr//td//font[2]")
        situacao = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[12]//tbody//tr//td[1]//font[2]")
        data_situacao = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[12]//tbody//tr//td[3]//font[2]")
        motivo_situacao = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[13]//tbody//tr//td//font[2]")
        situacao_especial = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[14]//tbody//tr//td[1]//font[2]")
        data_situacao_especial = handleData("//html//body//div[1]//div//div//div//div//div[2]//div//div//table[1]//tbody//tr//td//table[14]//tbody//tr//td[3]//font[2]")

        row_dict = preenche_dict(cnpj_code,inscricao,abertura,nome_empresarial,titulo_estabelecimento,porte,codigo_principal,codigo_secundario,codigo_juridico,logradouro,numero,complemento,cep,bairro,municipio,uf,endereco_eletronico,telefone,ente,situacao,data_situacao,motivo_situacao,situacao_especial,data_situacao_especial)

        print(row_dict)

        #manda pro arquivo
        append_to_csv(row_dict)
        
        # espera o botao voltar aparecer
        driver.find_element(By.CSS_SELECTOR, "button.btn.btn-secondary").click()

time.sleep(15)