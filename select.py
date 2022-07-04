import sqlite3
conexao = sqlite3.connect('sqlite3.dados')
sql = ''' 
SELECT id, nome, endereco, produto FROM fornecedores; 
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()