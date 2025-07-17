from coleta import coletar_produtos
from banco import salvar_no_banco, fechar_conexao
from excel import salvar_no_excel, iniciar_excel
from enviargmail import enviar_email

# Inicializa Excel
ws, wb, excel_path = iniciar_excel()

# Coleta os produtos
produtos = coletar_produtos(limite=5)

# Salva os produtos
for produto in produtos:
    if salvar_no_banco(produto):
        salvar_no_excel(ws, wb, excel_path, produto)

# Finaliza conexões
fechar_conexao()

# Envia e-mail com Excel
enviar_email(excel_path)

print("✅ Processo finalizado com sucesso.")
print(f"📁 Dados salvos em: {excel_path}")
