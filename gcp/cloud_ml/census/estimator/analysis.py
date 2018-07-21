import trainer.model as model
import pandas
import tensorflow as tf

train_file = "data/adult.data.csv"
test_file = "data/adult.test.csv"

#tf.enable_eager_execution()

# train_df = pandas.read_csv(train_file, header=None, names=model.CSV_COLUMNS)
# test_df = pandas.read_csv(test_file, header=None, names=model.CSV_COLUMNS)
#
# print(train_df.head())


ds = model.input_fn(filenames=[train_file], num_epochs=5, shuffle=True, batch_size=10)
