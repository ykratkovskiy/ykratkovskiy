import pandas as pd

df = pd.read_excel('material.xlsx', 'Лист1')
df.to_csv('material.csv', sep=';')
