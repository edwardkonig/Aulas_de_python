#!/usr/bin/python3
#coding: UTF-8

import csv

# definindo as perguntas
p = {
    "name": "Qual é o seu nome? ", 
    "age": "Qual é a sua idade? ",
    "gender": "Qual é o seu sexo? ",
    "city": "Onde você mora? "
}

# inciando as repostas
r = {
    "name": "", 
    "age": "",
    "gender": "",
    "city": ""
}

# função para aplicar o questionario
def aplicarQuestionario(perguntas, respostas):
    for questao, texto_questao in perguntas.items():
        if respostas[questao] == "":
            respostas[questao] = input(texto_questao)
    correcao(respostas)

# função para definir correção do questionário
def correcao(questionario):
    refazer = input("Quais perguntas gostaria de fazer? Digite os números separados por vírgula: ")
    for q in [list(questionario)[int(i) - 1] for i in refazer.split(",") if i != '']:
        questionario[q] = ""

# função para verificar o estado do questionario
def questionarioCompleto(questionario):
    return len([resposta for chave, resposta in questionario.items() if resposta == ""]) == 0

# função para salvar os dados no arquivo
def salvarCSV(arquivo, respostas):
    with open(arquivo, 'a+') as f:  
        w = csv.DictWriter(f, respostas.keys())
        if f.tell() == 0:
            w.writeheader()
        w.writerow(respostas)

# execução do programa
while not questionarioCompleto(r):
    aplicarQuestionario(p, r)

salvarCSV('respostas.csv', r)