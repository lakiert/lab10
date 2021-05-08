import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import xlrd
import openpyxl

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
# x = np.arange(0, 21, 1)
# y = (1/x)
# plt.plot(x, y, 'g>:', label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.ylim(0, 1)
# plt.xlim(0, len(x))
# plt.legend()
# plt.show()

# zad3
# x = np.arange(0, 30, 0.1)
# f = (np.sin(x))
# g = np.cos(x)
# plt.plot(x, f, x, g)
# plt.legend(['sin(x)', 'cos(x)'], loc='upper right')
# plt.yticks(np.arange(-1, 2, step=0.5))
# plt.xlabel('x')
# plt.ylabel('wartości sin(x) i cos(x)')
# plt.show()

# zad4
# x = np.arange(0, 30, 0.1)
# f = np.sin(x)+2
# g = -(np.sin(x))
# plt.plot(x, f, x, g)
# plt.yticks(np.arange(-1, 3.5, step=0.5))
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Wykres sin(x), sin(x)')
# plt.legend(['sin(x)', 'sin(x)'], loc='center left')
# plt.show()

# zad5
# df = pd.read_csv('iris.csv', names=['sepal len','sepal wid','petal len','petal wid', 'class'])
# df = pd.DataFrame(df)
# df = df[['sepal len','sepal wid', 'class']]
# print(df)
# # x = df['sepal len']
# # y = df['sepal wid']
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# data = {'a': df['sepal len'],
#         'b': df['sepal wid'],
#         'c': np.random.randint(0, 150, 150)}
# data['d'] = np.abs(data['a']-data['b'])
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.title('Iris sepal length and width')
# plt.show()



