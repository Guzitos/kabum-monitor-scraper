import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="cadu",
    database="vendaskabum"
)

cursor = conexao.cursor()

# Iniciar o navegador
navegador = webdriver.Chrome()
navegador.maximize_window()

# Variáveis de controle
pagina = 1
produtos_coletados = 0
limite = 10  # Alterar para 100 ou o quanto quiser

#Enquanto não bater o limite
while produtos_coletados < limite:
        url_pagina = f"https://www.kabum.com.br/computadores/monitores?page={pagina}"
        navegador.get(url_pagina)
        time.sleep(2)

        # Pega todos os cards de produto
        produtos = navegador.find_elements(By.CLASS_NAME, "productCard")

        if not produtos:
            print("❌ Nenhum produto encontrado. Encerrando.")
            break

        for produto in produtos:
            if produtos_coletados >= limite:
                break

            nome = produto.find_element(By.CLASS_NAME, "sc-27518a44-8").text
            preco = produto.find_element(By.CLASS_NAME, "sc-57f0fd6e-2").text

            try:
                avaliacao = produto.find_element(By.CLASS_NAME, "leading-none").text
            except:
                avaliacao = "(0)"

            try:
                frete = produto.find_element(By.CLASS_NAME, "w-max").text
            except:
                frete = "Sem frete grátis"

            try:
                desconto = produto.find_element(By.CLASS_NAME, "ary-500").text
            except:
                desconto = "Sem desconto"


            sql = "INSERT INTO monitores (nome, preco, desconto, avaliacao, frete_gratis) VALUES (%s, %s, %s, %s, %s)"
            valores = (nome, preco, desconto, avaliacao, frete)
            cursor.execute(sql, valores)
            conexao.commit()

            produtos_coletados += 1
            print(f"✅ Inserido: {produtos_coletados} - {nome}")

        try:
            cursor.execute(sql, valores)
            conexao.commit()
            produtos_coletados += 1
            print(f"✅ Inserido: {produtos_coletados} - {nome}")

        except mysql.connector.errors.IntegrityError:
            print(f"⚠️ Produto duplicado (não inserido): {nome}")
