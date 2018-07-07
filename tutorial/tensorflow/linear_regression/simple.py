import numpy as np
import tensorflow as tf

# Create feature column and estimator
column = tf.feature_column.numeric_column('x')
lin_reg = tf.estimator.LinearRegressor(feature_columns=[column])

# Train the estimator
train_input = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array([1.0, 2.0, 3.0, 4.0, 5.0])},
    y=np.array([2.0, 4.0, 6.0, 8.0, 10.0]), shuffle=False, num_epochs=None)
lin_reg.train(train_input, steps=2500)  ###Edited here

# Make two predictions
predict_input = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array([1.9, 1.4], dtype=np.float32)},
    num_epochs=1, shuffle=False)
results = lin_reg.predict(predict_input)

# Print result
for value in results:
    print(value['predictions'])
