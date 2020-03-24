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
    i = refazer + 1
    lista_respostas[i] = input (lista_perguntas[i])
    return refazer
        
            
# do_over_q()
termino = False
while not termino:
    refazer = correcao()
    if refazer == 0:
        termino = True

    

zipobj = zip(lista_perguntas, respostas)
d = dict(zipobj)
print(d)


        


''' 
Transformar tudo para dicionário/Como salvar as respostas de forma indexada? - Done
Como mostrar as infos para o usuário confirmar e depois retornar e fazer de novo?
Como que eu salvo no dicionário com nomes mais curtos?/cleaner code
https://thispointer.com/python-how-to-convert-a-list-to-dictionary/
 '''
