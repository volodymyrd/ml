import trainer.model as model
import pandas

train_file = "data/adult.data.csv"
test_file = "data/adult.test.csv"

train_df = pandas.read_csv(train_file, header=None, names=model.CSV_COLUMNS)
test_df = pandas.read_csv(test_file, header=None, names=model.CSV_COLUMNS)

print(train_df.head())
