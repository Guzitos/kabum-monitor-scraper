from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def coletar_produtos(limite=5):
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    pagina = 1
    coletados = 0
    produtos = []

    while coletados < limite:
        navegador.get(f"https://www.kabum.com.br/computadores/monitores?page={pagina}")
        time.sleep(2)
        cards = navegador.find_elements(By.CLASS_NAME, "productCard")

        if not cards:
            break

        for card in cards:
            if coletados >= limite:
                break

            nome = card.find_element(By.CLASS_NAME, "sc-27518a44-8").text
            preco = card.find_element(By.CLASS_NAME, "sc-57f0fd6e-2").text

            try: avaliacao = card.find_element(By.CLASS_NAME, "leading-none").text
            except: avaliacao = "(0)"

            try: frete = card.find_element(By.CLASS_NAME, "w-max").text
            except: frete = "Sem frete grátis"

            try: desconto = card.find_element(By.CLASS_NAME, "ary-500").text
            except: desconto = "Sem desconto"

            produtos.append({
                "nome": nome,
                "preco": preco,
                "avaliacao": avaliacao,
                "frete": frete,
                "desconto": desconto
            })
            coletados += 1

        pagina += 1

    navegador.quit()
    return produtos
