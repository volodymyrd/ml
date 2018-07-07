import matplotlib.pyplot as plt
import numpy as np

x = np.abs([1, 2, 3, 4, 5])
y = 2 * x + 5
plt.scatter(x, y)
plt.show()
