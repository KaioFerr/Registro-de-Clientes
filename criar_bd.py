import sqlite3

#criando conexão 
try:
    con = sqlite3.connect('Cadastro de clientes.db')
    print('Conexão com o banco de dados realizado com sucesso!')
except sqlite3.Error as e:
    print('Erro ao conectar com o banco de dados:', e)

#Criando tabela cliente
try:
    with sqlite3.connect('Cadastro_de_clientes.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT, 
            cnpj_cpf TEXT,
            endereco TEXT,
            contato TEXT,
            tipo_de_servico TEXT,
            preco REAL,  
            tipo_de_pagamento TEXT,
            status_do_pagamento TEXT
        )""")

        print("Tabela cliente criada com sucesso!")

except sqlite3.Error as e:
    print('Erro ao criar a tabela de cliente:', e)




