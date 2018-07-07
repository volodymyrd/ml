import argparse
import tensorflow as tf

import data

parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=1000, type=int, help='number of training steps')


def main(argv):
    args = parser.parse_args(argv[1:])

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = data.load_data()
    train_x = {'f': train_x}
    test_x = {'f': test_x}

    my_feature_columns = [tf.feature_column.numeric_column('f')]

    regression = tf.estimator.LinearRegressor(
        feature_columns=my_feature_columns,
        optimizer=tf.train.FtrlOptimizer(learning_rate=50.0))

    # Train the Model.
    # train_input = tf.estimator.inputs.numpy_input_fn(
    #     x=train_x,
    #     y=train_y, shuffle=True, num_epochs=None)
    # regression.train(train_input, steps=args.train_steps)
    regression.train(
        input_fn=lambda: data.train_input_fn(train_x, train_y, args.batch_size),
        steps=args.train_steps)

    # Evaluate the model.
    # evaluate_input = tf.estimator.inputs.numpy_input_fn(
    #     x=test_x,
    #     y=test_y, shuffle=False, num_epochs=1)
    # eval_result = regression.evaluate(evaluate_input, steps=args.train_steps)
    eval_result = regression.evaluate(
        input_fn=lambda: data.eval_input_fn(test_x, test_y, args.batch_size))
    print(eval_result)

    # predictions_input = tf.estimator.inputs.numpy_input_fn(
    #     x=train_x, shuffle=False, num_epochs=1)
    # predictions = regression.predict(input_fn=predictions_input)
    predictions = regression.predict(
        input_fn=lambda: data.eval_input_fn(test_x, labels=None, batch_size=args.batch_size))

    calc_y = []
    for pred_dict in predictions:
        calc_y.append(pred_dict['predictions'])

    print(calc_y)
    data.plot_data(test_x['f'], test_y, calc_y)


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
