'''
Created on 2020. 12. 26.

@author: Tristan Jin
'''
import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-9, 10)
y1 = x ** 2
plt.plot(
    x, y1,
    linestyle=":",
    marker="o",
    markersize=9,
    markerfacecolor="blue",
    markeredgecolor="red"
)

x = np.arange(-9, 10)
plt.bar(x, x ** 2)
plt.show()