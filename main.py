import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# zad1
# x = np.arange(0, 21, 1)
# y = (1/x)
# plt.plot(x, y, label='f(x)')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.ylim(0, 1)
# plt.xlim(1, len(x))
# plt.legend()
# plt.show()

# zad2
x = np.arange(0, 21, 1)
y = (1/x)
plt.plot(x, y, 'g>:', label='f(x) = 1/x')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.ylim(0, 1)
plt.xlim(0, len(x))
plt.legend()
plt.show()