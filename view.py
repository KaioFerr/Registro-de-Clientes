import sqlite3 as lite

#Criando conexão
try:
    con = lite.connect('Cadastro_de_clientes.db')
    print('Conexão com o banco de dados realizado com sucesso!')
except lite.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

#Criar Cliente (Inserir C)

def criar_cliente(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO clientes (nome, cnpj_cpf, endereco, contato, tipo_de_servico, preco, tipo_de_pagamento, status_do_pagamento) VALUES (?,?,?,?,?,?,?,?)" 
        cur.execute(query, i)


#Ver todos os clientes        
def ver_cliente():
    lista = []
    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM clientes')
        linha = cur.fetchall()

        for i in linha:
            lista.append(i)
    return lista


#Update do cliente
def update_cliente(i):
    with con:
        cur = con.cursor()
        query = "UPDATE clientes SET nome=?, cnpj_cpf=?, endereco=?, contato=?, tipo_de_servico=?, preco=?, tipo_de_pagamento=?, status_do_pagamento=? WHERE id=?" 
        cur.execute(query, i)


#Deletar os clientes
def deletar_cliente(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM clientes WHERE id=?" 
        cur.execute(query, i)


