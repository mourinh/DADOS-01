import sqlite3
conexao = sqlite3.connect('sqlite3.dados')
sql = ''' 
UPDATE fornecedores SET endereco = 'Rua dos Peixes, 26' WHERE id = 2
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()