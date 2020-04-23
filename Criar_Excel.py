import xlsxwriter
workbook = xlsxwriter.Workbook('dictExcel.xlsx')
worksheet = workbook.add_worksheet()
dict_perguntas = {
  "nome":  "Qual é o seu nome?", 
   "idade": "Qual é a sua idade?",
   "sexo": "Qual é o seu sexo?",
   "cidade": "Onde você mora?"
}

dict_respostas =  {}
  
name = input(dict_perguntas["nome"])
age = input (dict_perguntas["idade"])
sex = input(dict_perguntas["sexo"])
city = input(dict_perguntas["cidade"])
dict_respostas["nome"] = name
dict_respostas["idade"] = age
dict_respostas["sexo"] = sex
dict_respostas["cidade"] = city

def mergeDict(dict_perguntas, dict_respostas):
   dict_combined = {**dict_perguntas, **dict_respostas}
   for key, value in dict_combined.items():
       if key in dict_perguntas and key in dict_respostas:
               dict_combined[key] = [value , dict_perguntas[key]]
 
   return dict_combined
 
dict_combined = mergeDict(dict_perguntas, dict_respostas)
row = 0
col = 0

for key in dict_respostas.keys():
    row = 0
    worksheet.write(row, col, key)
    row += 1
    for item in dict_respostas[key]:
        worksheet.write(row, col, item)
        row += 1
    col += 1

workbook.close()

'''
https://thispointer.com/how-to-merge-two-or-more-dictionaries-in-python/
https://stackoverflow.com/questions/33575376/using-user-input-to-create-dictionaries-in-python
https://stackoverflow.com/questions/45201288/how-to-create-header-in-excel-from-a-python-dictionary-keys
'''
