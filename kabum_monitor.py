from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
import os

# Iniciar o navegador
navegador = webdriver.Chrome()
navegador.maximize_window()

# Variáveis de controle
pagina = 1
produtos_coletados = 0
limite = 3  # Alterar para 100 ou o quanto quiser

# Caminho do arquivo CSV
arquivo_xlsx = "monitores_kabum.xlsx"
existe = os.path.isfile(arquivo_xlsx)

# Abrir arquivo CSV
with open(arquivo_xlsx, mode='a', newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)

    # Cabeçalho
    if not existe:
        writer.writerow(["Nome", "Preço", "Avaliação", "Frete Grátis"])

    # Enquanto não bater o limite
    while produtos_coletados < limite:
        url_pagina = f"https://www.kabum.com.br/computadores/monitores?page={pagina}"
        navegador.get(url_pagina)
        time.sleep(3)

        # Pega todos os cards de produto
        produtos = navegador.find_elements(By.CLASS_NAME, "productCard")

        if not produtos:
            print("❌ Nenhum produto encontrado. Encerrando.")
            break

        for produto in produtos:
            if produtos_coletados >= limite:
                break

            try:
                nome = produto.find_element(By.CLASS_NAME, "sc-27518a44-8").text
            except:
                nome = "Nome não encontrado"

            try:
                preco = produto.find_element(By.CLASS_NAME, "sc-57f0fd6e-2").text
            except:
                preco = "Preço não encontrado"

            try:
                avaliacao = produto.find_element(By.CLASS_NAME, "text-xxs").text
            except:
                avaliacao = "(0)"

            try:
                frete = produto.find_element(By.CLASS_NAME, "h-16").text
            except:
                frete = "Sem frete grátis"

            writer.writerow([nome, preco, avaliacao, frete])
            produtos_coletados += 1
            print(f"✅ Produto {produtos_coletados}: {nome}")

        pagina += 1  # Próxima página

navegador.quit()
print("📁 Coleta finalizada. Dados salvos em:", arquivo_xlsx)
