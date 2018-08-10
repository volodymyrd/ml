"""Model"""

import tensorflow as tf

CSV_COLUMNS = ['date', 'time', 'open', 'max', 'min', 'close', 'vol']

INPUT_COLUMNS = [
    tf.feature_column.numeric_column('age'),
]
