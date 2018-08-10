import argparse
from model1 import model
import glob
import os
import pandas as pd

import tensorflow as tf
from tensorflow.contrib.learn.python.learn.utils import (
    saved_model_export_utils)
from tensorflow.contrib.training.python.training import hparam

import zipfile

THRESHOLD_FOR_OUTLIERS = 2


def remove_outliers(df, name):
    while True:
        index = df[df[name].rolling(2).apply(lambda x: abs(x[1] - x[0])) > THRESHOLD_FOR_OUTLIERS].index
        if index.size == 0:
            break
        df = df.loc[df.index != index[0]]
    return df


def unzip_file(path_to_arch, data_dir):
    zip_ref = zipfile.ZipFile(path_to_arch, 'r')
    zip_ref.extractall(data_dir)
    zip_ref.close()


def clean_dir(dir):
    files = glob.glob(dir + '/*')
    for f in files:
        os.remove(f)


def prepare_data(df, feature_window, label_window):
    """Run data preparation"""
    # print(df.tail())
    rows = df.shape[0]  # gives number of row count

    features = {}
    labels = {'min': [], 'max': []}
    for i in range(feature_window):
        features['f_open' + '_' + str(i)] = []
        features['f_close' + '_' + str(i)] = []
        features['f_min' + '_' + str(i)] = []
        features['f_max' + '_' + str(i)] = []

    for i, row in df.iterrows():
        if (i + feature_window + label_window) <= rows:
            index = 0
            for j, r in df.iloc[i:i + feature_window].iterrows():
                features['f_open' + '_' + str(index)].append(r['open'])
                features['f_close' + '_' + str(index)].append(r['close'])
                features['f_min' + '_' + str(index)].append(r['min'])
                features['f_max' + '_' + str(index)].append(r['max'])
                index += 1

            min = float('inf')
            max = 0
            for k, rl in df.iloc[i + feature_window:i + feature_window + label_window].iterrows():
                if min > rl['min']: min = rl['min']
                if max < rl['max']: max = rl['max']

            labels['min'].append(min)
            labels['max'].append(max)

        else:
            break

    print(features, labels)


def data_pre_processing(data_file_name, path_to_arch, data_dir):
    """Run data pre-processing"""

    # Clean data dir
    clean_dir(data_dir)
    print('Data dir cleaned.')

    unzip_file(path_to_arch + '/' + data_file_name + '.zip', data_dir)

    df = pd.read_csv(data_dir + '/' + data_file_name + '.csv', header=None, names=model.CSV_COLUMNS)
    df['date_time'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%Y.%m.%d %H:%M')
    df.index = df['date_time']
    print(df.shape)

    df = remove_outliers(df, 'open')
    print(df.shape)
    df = remove_outliers(df, 'min')
    print(df.shape)
    df = remove_outliers(df, 'max')
    print(df.shape)
    df = remove_outliers(df, 'close')
    print(df.shape)
    return df


def build_data_file_name(pair, time_interval, data_period):
    return pair + '_' + time_interval + '_' + data_period


def run_experiment(hparams):
    """Run the training and evaluate using the high level API"""

    data_file_name = build_data_file_name(hparams.pair, hparams.time_interval, hparams.data_period)

    df = data_pre_processing(data_file_name, hparams.path_to_archives, hparams.path_to_data_dir)

    prepare_data(df)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # Input Arguments
    parser.add_argument(
        '--pair',
        help='Currency pair',
        default='EURPLN'
    )
    parser.add_argument(
        '--time_interval',
        help='Time interval',
        default='60'
    )
    parser.add_argument(
        '--data_period',
        help='Period for data',
        default='2005-07-21_2018-08-07'
    )
    parser.add_argument(
        '--path_to_archives',
        help='Path to data archives (zip-format)',
        default='/Users/vova/work/workspace/ml/utils'
    )
    parser.add_argument(
        '--path_to_data_dir',
        help='Path to data directory',
        default='/Users/vova/work/workspace/ml/fx/data'
    )

    # Argument to turn on all logging
    parser.add_argument(
        '--verbosity',
        choices=[
            'DEBUG',
            'ERROR',
            'FATAL',
            'INFO',
            'WARN'
        ],
        default='INFO',
    )

    args = parser.parse_args()

    # Set python level verbosity
    tf.logging.set_verbosity(args.verbosity)
    # Set C++ Graph Execution level verbosity
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = str(
        tf.logging.__dict__[args.verbosity] / 10)

    # Run the training job
    hparams = hparam.HParams(**args.__dict__)
    run_experiment(hparams)
