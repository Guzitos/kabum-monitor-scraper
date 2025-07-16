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
git clone https://github.com/seu-usuario/kabum-monitor-scraper.git
cd kabum-monitor-scraper
```

### 2. Instale as dependências
```bash
pip install selenium mysql-connector-python
```

### 3. Configure o banco de dados MySQL
No seu MySQL, crie o banco e a tabela:
```bash
CREATE DATABASE vendaskabum;

USE vendaskabum;

CREATE TABLE monitores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) UNIQUE,
  preco VARCHAR(50),
  desconto VARCHAR(50),
  avaliacao VARCHAR(50),
  frete_gratis VARCHAR(100)
);
```
### 4. Agora no python atualize suas credenciais no código
No trecho:

conexao = mysql.connector.connect(
    host="localhost",
    user="SEU_USUARIO",
    password="SUA_SENHA",
    database="vendaskabum"
)

### 5. Execute o script
```bash
python kabum_monitor.py
