import sqlite3
conexao = sqlite3.connect('sqlite3.dados')
sql = ''' 
INSERT INTO fornecedores (id, nome, endereco, produto) 
VALUES (5, 'Padaria do Pão', 'Rua das Carnes 56', 'Pão');
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()
