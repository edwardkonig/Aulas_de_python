arquivo = ''

with open('mycsvfile.csv') as f:  
    line = f.readline()
    while line != '':
        arquivo += line
        line = f.readline()

print(arquivo)