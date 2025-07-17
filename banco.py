import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conexao.cursor()

def salvar_no_banco(produto):
    cursor.execute("SELECT id FROM monitores WHERE nome = %s", (produto["nome"],))
    cursor.fetchall()

    if cursor.rowcount > 0:
        print(f"⚠️ Produto já existe: {produto['nome']}")
        return False

    sql = "INSERT INTO monitores (nome, preco, desconto, avaliacao, frete_gratis) VALUES (%s, %s, %s, %s, %s)"
    dados = (produto["nome"], produto["preco"], produto["desconto"], produto["avaliacao"], produto["frete"])
    cursor.execute(sql, dados)
    conexao.commit()
    print(f"✅ Inserido no banco: {produto['nome']}")
    return True

def fechar_conexao():
    cursor.close()
    conexao.close()
