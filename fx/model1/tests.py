import pandas as pd
from model1 import task


def test_hidden_layers_generator():
    for hl in task.hidden_layers_generator(4, 5, 9, 11):
        print(hl)


def test_get_out_put_dir():
    for hl in task.hidden_layers_generator(4, 5, 9, 11):
        print(task.get_out_put_dir(hl))


def test1():
    """test1"""
    data = {'open': [4.2, 4.25, 4.3, 4.2, 4.4, 4.3, 4.35],
            'close': [4.2, 4.25, 4.3, 4.2, 4.4, 4.3, 4.35],
            'min': [4.2, 4.25, 4.3, 4.2, 4.4, 4.3, 4.35],
            'max': [4.2, 4.25, 4.3, 4.2, 4.4, 4.3, 4.35]}

    df = pd.DataFrame(data)
    print(task.prepare_data(df, 3, 2))


def tests():
    test1()


if __name__ == '__main__':
    # tests()
    # test_hidden_layers_generator()
    test_get_out_put_dir()
