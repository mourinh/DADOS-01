
import sqlite3
conexao = sqlite3.connect('sqlite3.dados')
sql = ''' 
DELETE FROM fornecedores WHERE id = 3;
'''
cursor = conexao.cursor()
cursor.execute(sql)
conexao.commit()
conexao.close()