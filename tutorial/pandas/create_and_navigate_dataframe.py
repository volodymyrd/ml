import pandas as pd

data = {'col_1': [1, 2, 3, 4, 5],
        'col_2': [5, 4, 3, 2, 1],
        'col_3': [10, 9, 8, 7, 6],
        'col_4': [2, 4, 6, 8, 10],
        'col_5': [1, 3, 5, 7, 9], }

df = pd.DataFrame(data)
print(df)
print(df.dtypes)
print(df['col_2'])
print(df['col_2'][1])
exit()
