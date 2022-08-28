import pyodbc 
from os import system 
system('cls')


# Função de conexão com o banco de dados
def conexao(server , database, username, password):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    return conn

# Função para insert tabela
def inserir(cidade, pontuacao):
    inserir = f"INSERT INTO teste(cidade, pontuacao) VALUES ('{cidade}', '{pontuacao}')"
    return inserir

def buscar():
    select_buscar = f"SELECT * FROM teste"
    exec_select_buscar = cursor.execute(select_buscar)
    for linha in exec_select_buscar:
        print(linha)

def deletar(nome):
    select_deletar = f"DELETE FROM teste WHERE cidade = '{nome}'"
    cursor.execute(select_deletar)
    cursor.commit()

cursor = conexao('DESKTOP-PNLMOAP', 'escola', 'sa', '123')
cursor.cursor()

# deletar('itapevi')

while True:
    cidade = input('Cidade: ')
    pontuacao = input('Pontuação: ')
    print()

    if cidade == '' and pontuacao == '':
        break
    
    cadastrar = inserir(cidade, str(pontuacao))
    cursor.execute(cadastrar)
    cursor.commit()

buscar()





