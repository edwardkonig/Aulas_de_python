#!/usr/bin/python3
#coding: UTF-8

import csv

perguntas = {
    "name": "Qual é o seu nome? ", 
    "age": "Qual é a sua idade? ",
    "gender": "Qual é o seu sexo? ",
    "city": "Onde você mora? ",
    "dog_name": "Qual o nome do seu cachorro? "
}

# Poderíamos gerar um dicinário novo assim:

# respostas = {
#     "name": "", 
#     "age": "",
#     "gender": "",
#     "city": ""
# }

# Mas o modo mais "pythonista" seria:
respostas = dict.fromkeys(perguntas.keys(), "")

# fazendo a pergunta iterando o dicionário
# for key in perguntas:
#     value = perguntas[key]
    # resposta = input(value)
    # respostas[key] = resposta
# Mas iterar o dicionário retorna somente as chaves, podemos então usar o método .items() para pegar cada item como um tupla
# for item in perguntas.items():
#     key = item[0]
#     value = item[1]
#     resposta = input(value)
#     respostas[key] = resposta
# Já que estamos manipulando uma tupla, podemos "desenpacotar" (unpack) -- super pythônico!
# for k, v in perguntas.items():
#     r = input(v)
#     respostas[k] = r
# Podemos otimizar ainda mais, sem que isso signifique perder "legibilidade"
for questao, texto_questao in perguntas.items():
    repostas[questao] = input(texto_questao)

# def do_over_q():
#     do_over = int (input("Qual pergunta gostaria de refazer? Por favor selecione um número correspondente à pergunta a ser refeita"))
#     i = do_over
#     for i in range(0,4):
#         if do_over == i+1:
#             lista_respostas[i] = input (lista_perguntas[i]) 
#             break
            
# def correcao():
#     refazer = int(input("Qual pergunta gostaria de refazer? Por favor selecione um número correspondente à pergunta a ser refeita"))
#     i = refazer - 1
#     if refazer != 0:
#         lista_respostas[i] = input (lista_perguntas[i])
#     return refazer     
            
# # do_over_q()
# termino = False
# while not termino:
#     refazer = correcao()
#     if refazer == 0:
#         termino = True

# Esse loop de perguntar e responder uma por uma pode melhorar
# def correcao():
#     refazer = input("Quais perguntas gostaria de fazer? Digite os números separados por vírgula")
#     for i in refazer.split(","):
#         if i != '':
#             i = int(i) - 1
#             respostas[i] = input(perguntas[i])

# correcao()

# Mas pq não funcionou?? Por que não temos mais listas, e sim dicionários!!
def correcao():
    refazer = input("Quais perguntas gostaria de fazer? Digite os números separados por vírgula: ")
    for i in refazer.split(","):
        if i != '':
            questao = list(perguntas)[int(i) - 1]
            respostas[questao] = input(perguntas[questao])

correcao()

# como sabemos se acabou de uma forma melhor? - ABSURDAMENTE PYTHONISTA
def questionarioCompleto(questionario):
    return len([resposta for chave, resposta in questionario.items() if resposta == ""]) == 0

# print(questionarioCompleto(respostas))

#  - Mas que P***A foi essa professor???
# Foi a tal da Compreensão de Listas (List Comprehension)
# Mas seria possível fazer assim:
# def questionarioCompleto2(questionario):
#     incompletas = []
#     for chave, resposta in questionario.items():
#         if resposta == "":
#             incompletas.append(resposta)
    
#     if len(incompletas) == 0:
#         return True
#     else:
#         return False

# print(questionarioCompleto2(respostas))



# Mas oq fazemos com isso agora???
# while not questionarioCompleto(respostas):
    # for questao, texto_questao in perguntas.items():
    #     if respostas[questao] == "":
    #         respostas[questao] = input(texto_questao)
    # correcao()

# Qual o problema disso?? Estou repetindo código!!
def aplicarQuestionario(p, r):
    for q, t in p.items():
        if r[q] == "":
            r[q] = input(t)

# E posso inclusive comentar o código pra primeira aplicação
#  - Mas eu precisava da função aplicarQuestionario()?
# Função nunca é d+
while not questionarioCompleto(respostas):
    aplicarQuestionario(perguntas, respostas)
    correcao()

with open('respostas.csv', 'a+') as f:  
    w = csv.DictWriter(f, respostas.keys())
    if f.tell() == 0:
        w.writeheader()
    w.writerow(respostas)