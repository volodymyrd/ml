import numpy as np

a = np.arange(5, 20)
print(a)
s = slice(2, 9, 3)
print(a[s])

print('-----')
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x.shape, '\n', x[1:7:2])

print('-----')
x = np.array([[[1], [2], [3]], [[4], [5], [6]]])
print(x.shape, '\n', x)
nx = x[:, np.newaxis, :, :]
print(nx.shape, '\n', nx)

print('-----')
x = np.array([[1, 3, 5, 7], [2, 4, 6, 8]])
print(x.shape, '\n', x)
nx = x[:, 0]
print(nx.shape, '\n', nx)
nx = nx[:, np.newaxis]
print(nx.shape, '\n', nx)
print(np.array_equal(nx, x[:, np.newaxis, 0]))
nx = x[:, np.newaxis, 0]
print(nx.shape, '\n', nx)

