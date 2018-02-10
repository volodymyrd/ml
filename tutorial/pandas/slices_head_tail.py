import pandas as pd

data = {'col_1': [1, 2, 3, 4, 5, 6, 7],
        'col_2': [5, 4, 3, 2, 1, 0, -1],
        'col_3': [10, 9, 8, 7, 6, 5, 4],
        'col_4': [2, 4, 6, 8, 10, 12, 14],
        'col_5': [1, 3, 5, 7, 9, 11, 13], }

df = pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df['col_1'][0])