import smtplib
import os
from email.message import EmailMessage

def enviar_email():

    from kabum_monitor import excel_path

    # Configurações do remetente
    email_remetente = 'emailRemetente@gmail.com'
    senha = 'sua_senha' # Atalho: https://myaccount.google.com/apppasswords
    email_destinatario = 'emailDestinatario@gmail.com'

    # Criar o e-mail
    msg = EmailMessage()
    msg['Subject'] = 'Assunto do Email'
    msg['From'] = email_remetente
    msg['To'] = email_destinatario
    msg.set_content('Olá! Este é o corpo do email com um anexo.')

    # Caminho do arquivo a ser anexado

    caminho_arquivo = excel_path  # substitua pelo nome do seu arquivo
    nome_arquivo = os.path.basename(caminho_arquivo)

    # Ler e anexar o arquivo
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

    print("E-mail enviado com sucesso!")

