import csv
name = input("Insira o nome de quem está procurando")
# with open('mycsvfile.csv') as csvfile:
#     reader = csv.reader(csvfile, delimiter = ',')
csv_file = csv.reader(open('mycsvfile.csv'), delimiter=",")
for row in csv_file:
    if name == row[0]:
        print(' , '.join(row))