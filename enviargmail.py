import smtplib
import os
from email.message import EmailMessage

def enviar_email(caminho_arquivo):
    # Configurações do remetente
    email_remetente = 'gmail.com'
    senha = 'sua_senha' #atalho https://myaccount.google.com/apppasswords
    email_destinatario = 'gmail.com'

    # Criar o e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Relatório Kabum'
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg.set_content('Olá! Este é o corpo do email com um anexo.')

    # Anexar o arquivo
    nome_arquivo = os.path.basename(caminho_arquivo)

    with open(caminho_arquivo, 'rb') as arquivo:
        conteudo = arquivo.read()
        msg.add_attachment(
            conteudo,
            maintype='application',
            subtype='octet-stream',
            filename=nome_arquivo
        )

    # Enviar o e-mail
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_remetente, senha)
        smtp.send_message(msg)

    print("📧 E-mail enviado com sucesso!")
