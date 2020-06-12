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
conn.execute('''CREATE TABLE CADASTRO
         (ID INT PRIMARY KEY     NOT NULL,
         NOME           TEXT    NOT NULL,
         IDADE            INT     NOT NULL,
         SEXO            TEXT
         CIDADE         TEXT);''')
cursor = conn.execute("SELECT id, nome, idade, sexo, cidade from CADASTRO")

for key,value in dict_respostas.items():
    count = 1
    conn.execute("INSERT INTO CADASTRO (ID, NOME, IDADE, SEXO, CIDADE) \
        VALUES (count,dict_respostas[nome],dict_respostas[idade],dict_respostas[sexo],dict_respostas[cidade])
    count+=1