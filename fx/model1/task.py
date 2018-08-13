import argparse
from model1 import model
import glob
import itertools
import os
import pandas as pd

import tensorflow as tf
from tensorflow.contrib.learn.python.learn.utils import (
    saved_model_export_utils)
from tensorflow.contrib.training.python.training import hparam

import zipfile

THRESHOLD_FOR_OUTLIERS = 2


def get_out_put_dir(hidden_units_array):
    path = ''
    for unit in hidden_units_array:
        path += '_' + str(unit)
    return path


def hidden_layers_generator(
        number_of_layers_min=1, number_of_layers_max=2, number_of_neurons_min=1, number_of_neurons_max=2):
    for layers in range(number_of_layers_min, number_of_layers_max):
        for hidden_units in itertools.product(range(number_of_neurons_min, number_of_neurons_max), repeat=layers):
            hidden_units_list = list(hidden_units)
            yield hidden_units_list


def extract_features_and_labels(df, feature_window, label_window):
    """Extract features and labels"""

    rows = df.shape[0]  # gives number of row count

    features = {}
    labels = {'min': [], 'max': []}

    for i in range(feature_window):
        features['f_open' + '_' + str(i)] = []
        features['f_close' + '_' + str(i)] = []
        features['f_min' + '_' + str(i)] = []
        features['f_max' + '_' + str(i)] = []

    row_number = 0
    for _ in df.itertuples():
        if (row_number + feature_window + label_window) <= rows:
            index = 0
            for r in df[row_number:row_number + feature_window].itertuples():
                features['f_open' + '_' + str(index)].append(r.open)
                features['f_close' + '_' + str(index)].append(r.close)
                features['f_min' + '_' + str(index)].append(r.min)
                features['f_max' + '_' + str(index)].append(r.max)
                index += 1

            min = float('inf')
            max = 0
            for rl in df[row_number + feature_window:row_number + feature_window + label_window].itertuples():
                if min > rl.min: min = rl.min
                if max < rl.max: max = rl.max

            labels['min'].append(min)
            labels['max'].append(max)

            row_number += 1
        else:
            break

    return features, labels


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


def clean_dir(path_to_dir):
    files = glob.glob(path_to_dir + '/*')
    for f in files:
        os.remove(f)


def prepare_data(df, feature_window, label_window):
    """Run data preparation"""

    df_rows = df.shape[0]

    train = extract_features_and_labels(df[:df_rows - 1], feature_window, label_window)

    test = extract_features_and_labels(df[df_rows - (feature_window + label_window):],
                                       feature_window, label_window)
    return train, test


def data_pre_processing(data_file_name, path_to_arch, data_dir):
    """Run data pre-processing"""

    # Clean data dir
    clean_dir(data_dir)
    print('Data dir cleaned.')

    unzip_file(path_to_arch + '/' + data_file_name + '.zip', data_dir)

    df = pd.read_csv(data_dir + '/' + data_file_name + '.csv', header=None, names=model.CSV_COLUMNS)
    df['date_time'] = pd.to_datetime(df['date'] + ' ' + df['time'], format='%Y.%m.%d %H:%M')
    df.index = df['date_time']
    df.sort_index(inplace=True)
    print(df.shape)

    df = remove_outliers(df, 'open')
    print(df.shape)
    df = remove_outliers(df, 'min')
    print(df.shape)
    df = remove_outliers(df, 'max')
    print(df.shape)
    df = remove_outliers(df, 'close')
    print(df.shape)
    # df.index = range(df.shape[0])
    return df


def build_data_file_name(pair, time_interval, data_period):
    return pair + '_' + time_interval + '_' + data_period


def run_experiment(hparams):
    """Run the training and evaluate using the high level API"""

    data_file_name = build_data_file_name(hparams.pair, hparams.time_interval, hparams.data_period)

    df = data_pre_processing(data_file_name, hparams.path_to_archives, hparams.path_to_data_dir)

    train, test = prepare_data(df, hparams.feature_window, hparams.label_window)

    print(test)
    # my_feature_columns = [tf.feature_column.numeric_column('f')]
    # estimator = tf.estimator.DNNClassifier(
    #     feature_columns=[],
    #     hidden_units=[1024, 512, 256])

    estimator = tf.estimator.DNNRegressor()


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

    parser.add_argument(
        '--feature_window',
        help='Window for features',
        type=int,
        default=5
    )

    parser.add_argument(
        '--label_window',
        help='Window for labels',
        type=int,
        default=4
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
