import pandas as pd

file_path = 'data.xlsx'
df = pd.read_excel("Книга4.xlsx")
column_index = int(input("\nВведите индекс столбца для вычисления среднего арифметического (начиная с 1): "))

if 1 <= column_index <= len(df.columns):

    column_name = df.columns[column_index - 1]

    if pd.api.types.is_numeric_dtype(df[column_name]):

        mean_value = df[column_name].mean()
kvadotklon = (column_index - mean_value)
print(f"Дисперсия столбца:" sum[kvadotklon] / len[column_index])