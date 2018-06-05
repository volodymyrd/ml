import traceback
import pandas as pd
import tensorflow as tf

print(tf.__version__)

DATA_SET = '/Users/vova/Downloads/forex/EURPLN_60_1997-01-01_2018-05-29.csv'
CSV_COLUMNS = ['date', 'time', 'open', 'max', 'min', 'close', 'vol']
THRESHOLD_FOR_OUTLIERS = 2


def data_preprocessing():
    df_all = pd.read_csv(DATA_SET, header=None, names=CSV_COLUMNS)
    df_all['date_time'] = pd.to_datetime(df_all['date'] + ' ' + df_all['time'], format='%Y.%m.%d %H:%M')
    df_all.index = df_all['date_time']
    print(df_all.shape)
    print(df_all.head(5))

    df_all = remove_outliers(df_all, 'max')
    print(df_all.shape)
    df_all = remove_outliers(df_all, 'min')
    print(df_all.shape)


def remove_outliers(df, name):
    while True:
        index = df[df[name].rolling(2).apply(lambda x: abs(x[1] - x[0]), raw=True) > THRESHOLD_FOR_OUTLIERS].index
        if index.size == 0:
            break
        df = df.loc[df.index != index[0]]
    return df

if __name__ == '__main__':

    # Run the training job:
    try:
        data_preprocessing()
    except:
        traceback.print_exc()
