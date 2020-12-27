import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10) #아래 막대
y = np.random.rand(10) #중간
z = np.random.rand(10) #위
data = [x, y, z]
print(x)
x_array = np.arange(10)
for i in range(0,3):
    plt.bar(
        x_array,
        data[i],
        bottom=np.sum(data[:i],axis=0)
    )
plt.show()

x = np.random.rand(10)
y = np.random.rand(10)
colors = np.random.randint(0,100,10)
print(colors)
sizes = np.pi * 1000 * np.random.rand(10)
plt.scatter(x, y, c=colors, s=sizes, alpha=0.7)
plt.show()