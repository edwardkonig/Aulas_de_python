import csv
# name = input("Insira o nome de quem está procurando")
# with open('mycsvfile.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter = ',')
csv_file = csv.reader(open('fichas.csv'), delimiter=",")
# for row in csv_file:
#     # if name == row[0]:
#     #     print(' , '.join(row))
#     print(row[0].sort())
lista = []
troca = False
for row in csv_file:
    lista.append(row)

for i in range(len(lista) - 1):
    item = lista[i]
    proximo_item = lista[i+1]
    if item[0] > proximo_item[0]:
        lista[i+1], lista[i]  = item, proximo_item

for linha in lista:
    print(linha)

'''
Biblioteca de excel e conseguir gerar arquivo em Excel, manipulando tudo
Manipule dicionário para que o cabeçalho seja referenciado (a lista de perguntas tem que ser um dicionário)
'''