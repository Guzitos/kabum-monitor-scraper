### 🖥️ Kabum Monitor – Raspagem de Monitores com Python
Projeto feito em Python para raspagem automática de dados do site Kabum, armazenando os resultados em:

Um banco de dados MySQL

Um arquivo Excel (.xlsx)

E enviando um e-mail automático com o Excel em anexo

📌 Funcionalidades
✅ Raspagem de monitores com Selenium

✅ Armazenamento no MySQL para evitar duplicados

✅ Exportação para planilha Excel

✅ Envio automático por e-mail com anexo

✅ Executável .exe para rodar com duplo clique

### 🧱 Tecnologias utilizadas
Python 3.13

Selenium

openpyxl

MySQL (via mysql-connector-python)

smtplib (e-mail)

PyInstaller (para criar o .exe)


📦 Como rodar o projeto localmente

### 1. Clone o repositório:
```
git clone https://github.com/seu-usuario/kabum-monitor.git
cd kabum-monitor
````

### 3. Instale as dependências:
```
pip install -r requirements.txt
```

### 4. Configure seu banco MySQL:
Crie um banco chamado vendaskabum e uma tabela monitores:
```
CREATE DATABASE vendaskabum;

USE vendaskabum;

CREATE TABLE monitores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    preco VARCHAR(50),
    desconto VARCHAR(50),
    avaliacao VARCHAR(20),
    frete_gratis VARCHAR(50)
);
```

### 5. Atualize as credenciais do e-mail
No arquivo enviargmail.py, substitua:
```
email_remetente = 'seu_email@gmail.com'
senha = 'sua_senha_de_app'
Você pode gerar uma senha de app aqui: https://myaccount.google.com/apppasswords
```

### 6. Execute o projeto:
python kabum_monitor.py
📁 Estrutura do projeto

ChatBot/
├── kabum_monitor.py         # Script principal

├── coleta.py                # Raspagem com Selenium

├── banco.py                 # Interação com MySQL

├── excel.py                 # Controle do Excel

├── enviargmail.py           # Envio de e-mail com anexo

├── monitores_kabum.xlsx     # Planilha gerada (opcional)

├── README.md                # Este arquivo

🧪 Gerar .exe (opcional)
Para criar um .exe e rodar com duplo clique:
```
pip install pyinstaller
pyinstaller --onefile kabum_monitor.py
O executável ficará na pasta dist/.
```

📬 Contato
Feito por Gustavo Rodrigues

Se quiser trocar ideias, me chama por aqui!
