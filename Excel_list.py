import pandas as pd

# Paths to your excel files
excel_file_1 = 'path to excel file 1'
excel_file_2 = 'path to excel file 2'

# Read the files
df1 = pd.read_excel(excel_file_1)
df2 = pd.read_excel(excel_file_2)
list1 = df1['column 1'].values.tolist()
list2 = df2['column 1'].values.tolist()
difference1 = list(set(list1) - set(list2))
difference2 = list(set(list2) - set(list1))
print(difference1)
print(difference2)


