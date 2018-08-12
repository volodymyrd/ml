import pandas as pd
from model1 import task


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
    tests()
