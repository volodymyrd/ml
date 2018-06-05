import pandas as pd
import matplotlib.pyplot as plt


def group(val):
    if val > 0.2:
        return 0.2
    elif val > 0.1:
        return 0.1
    elif val > 0.05:
        return 0.05
    elif val > 0.01:
        return 0.01
    else:
        return 0.0


pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
df = pd.read_csv('/Users/vova/Downloads/forex/EURPLN_60_1997-01-01_2018-05-29.csv', header=None,
                 names=['date', 'time', 'open', 'max', 'min', 'close', 'vol'])
df['date_time'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%Y.%m.%d %H:%M')
df.index = df['date_time']
print(df.shape)
# print(df.head(5))

while True:
    index = df[df['max'].rolling(2).apply(lambda x: abs(x[1] - x[0])) > 2].index
    if index.size == 0:
        break

    # print(df.loc[[index[0]]])
    df = df.loc[df.index != index[0]]

print(df.shape)
print(df.head(10))

while True:
    index = df[df['min'].rolling(2).apply(lambda x: abs(x[1] - x[0])) > 2].index
    if index.size == 0:
        break

    print(df.loc[[index[0]]])
    df = df.loc[df.index != index[0]]

print(df.shape)
#
# df['max_mean'] = df['max'].rolling(5).mean()
# print(df.head(10))
# df['dif'] = df['max'] - df['max_mean'].shift(1)
# print(df.head(10))

# new_sample_df = df.loc['2008-06-20', ['max', 'close', 'min']]
# new_sample_df.plot()
# plt.show()
# print(new_sample_df)

# df1 = (df.resample('D')['max'].max() - df.resample('D')['min'].min())
# # print(type(df1))
# # print(df1.shape)
# df1 = df1.sort_values(ascending=False)
# # print(df1.head(17))
# print(df1.size)
# df1 = 100.0 * (df1.groupby(lambda x: group(df1[x])).size() / df1.size)
# print(df1.head(5))

df_date = pd.Series((df['date_time'].values.reshape(-1, 5))[:, 4], name='date_time')
df_data = pd.DataFrame(df['max'].values.reshape(-1, 5))
print(df_date.shape)
print(df_data.shape)
df_new = pd.concat([df_date, df_data], axis=1)
print(df_new.head())
