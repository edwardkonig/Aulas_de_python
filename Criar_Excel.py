import xlsxwriter
import pandas as pd
import numpy as np
 workbook = xlsxwriter.Workbook('cadastro.xlsx')
 worksheet = workbook.add_worksheet()



df_new = pd.read_csv('fichas.csv')
writer = pd.ExcelWriter('cadastro.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1',startrow = 1, header = False)
writer.save()