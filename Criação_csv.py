import csv

lista_perguntas = [
   "Qual é o seu nome?", 
   "Qual é a sua idade?",
   "Qual é o seu sexo?",
   "Onde você mora?"
  ]

lista_respostas = []

for pergunta in lista_perguntas:
    resposta = input(pergunta)
    lista_respostas.append(resposta)


def do_over_q():
    do_over = int (input("Qual pergunta gostaria de refazer? Por favor selecione um número correspondente à pergunta a ser refeita"))
    i = do_over
    for i in range(0,4):
        if do_over == i+1:
            lista_respostas[i] = input (lista_perguntas[i]) 
            break
            
def correcao():
    refazer = int(input("Qual pergunta gostaria de refazer? Por favor selecione um número correspondente à pergunta a ser refeita"))
    i = refazer - 1
    if refazer != 0:
        lista_respostas[i] = input (lista_perguntas[i])
    return refazer
        
            
# do_over_q()
termino = False
while not termino:
    refazer = correcao()
    if refazer == 0:
        termino = True

    

zipobj = zip(lista_perguntas, lista_respostas)
d = dict(zipobj)
print(d)

# arquivo = ''

# with open('mycsvfile.csv') as f:  
#     line = f.readline()
#     while line != '':
#         arquivo += line
#         line = f.readline()

with open('mycsvfile.csv', 'a+') as f:  
    w = csv.DictWriter(f, d.keys())
    if f.tell() == 0:
        w.writeheader()
    w.writerow(d)
    #  w = csv.DictWriter(f, d.keys())
    # if arquivo == '':
    #     w.writeheader()
    #  else:
    #      f.write(arquivo)
    # w.writerow(d)
    # f.write(arquivo)
    # f.writelines(str(d.dict_values))
        


''' 
Transformar tudo para dicionário/Como salvar as respostas de forma indexada? - Done
Como mostrar as infos para o usuário confirmar e depois retornar e fazer de novo?
Como que eu salvo no dicionário com nomes mais curtos?/cleaner code
https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
 '''
'''
Desafio aula 2:
Estudar documentação da função open() para salvar um arquivo com as respostas do questionário
Acumular informações no documento sem perder nenhuma anterior
Salvar informações como csv
https://stackoverflow.com/questions/10373247/how-do-i-write-a-python-dictionary-to-a-csv-file
https://docs.python.org/3/library/functions.html#open
'''

'''
Desafio Aula 3:
Arrumar bagunça, a+
Como saber se escreve o header ou não (as chaves do dicionário), chave -> valor.... (biblioteca csv)
Fazer um outro arquivo Python que busque dentro do arquivo csv uma ficha qualquer
https://stackoverflow.com/questions/28325622/python-csv-writing-headers-only-once
https://stackoverflow.com/questions/26082360/python-searching-csv-and-return-entire-row/26082493
https://docs.python.org/3/library/csv.html
'''
