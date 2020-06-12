import sqlite3
dict_perguntas = {
  "nome":  "Qual é o seu nome?", 
   "idade": "Qual é a sua idade?",
   "sexo": "Qual é o seu sexo?",
   "cidade": "Onde você mora?"
}
dict_respostas = dict.fromkeys(dict_perguntas.keys(), "") # e se fosse um valor com string cheia?

for k,v in dict_perguntas.items():
    r = input(v)
    dict_respostas[k]= r


conn = sqlite3.connect('cadastro.db')
# conn.execute('''CREATE TABLE FICHA
#          (NOME           TEXT    NOT NULL,
#          IDADE           INT    NOT NULL,
#          SEXO            TEXT   NOT NULL,
#          CIDADE         TEXT    NOT NULL);''')
# cursor = conn.execute("SELECT ID, NOME, IDADE, SEXO, CIDADE from FICHA")
list_aspas = []
for value in dict_respostas.values():
    aspas_valor = "'{}'".format(value)
    list_aspas.append(aspas_valor)

query = "INSERT INTO FICHA ({}) VALUES ({})".format(','.join(dict_perguntas.keys()), ','.join(list_aspas))
conn.execute(query)
conn.commit()
#  (ID INT PRIMARY KEY     NOT NULL,

'''
https://stackoverflow.com/questions/14108162/python-sqlite3-insert-into-table-valuedictionary-goes-here
https://www.tutorialspoint.com/sqlite/sqlite_python.htm
'''