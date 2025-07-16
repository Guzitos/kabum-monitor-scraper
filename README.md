# 📊 Kabum Monitor Scraper

Este projeto realiza a raspagem de dados de monitores do site da [Kabum](https://www.kabum.com.br) utilizando **Selenium** e armazena as informações diretamente em um banco de dados **MySQL**. A estrutura está pronta para ser usada em análises, automações ou integração com dashboards.

---

## 🚀 Funcionalidades

- Raspagem de dados com Selenium (nome, preço, avaliação, frete e desconto)
- Paginação automática para coletar múltiplos produtos
- Integração com banco de dados MySQL
- Prevenção de dados duplicados via checagem no banco
- Totalmente automatizável para uso diário ou em servidores

---

## 🧰 Tecnologias utilizadas

- Python 3.x
- [Selenium](https://selenium.dev/)
- [MySQL](https://www.mysql.com/)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- Google Chrome + ChromeDriver

---

## 🛠️ Como executar o projeto

### 1. Clone o repositório
```bash
git clone https://github.com/guzitos/kabum-monitor-scraper.git
cd kabum-monitor-scraper
