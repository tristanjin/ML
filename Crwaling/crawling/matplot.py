import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3]
y = [1,2,3]

plt.plot(x,y)
plt.title("My plot")
plt.xlabel("X")
plt.ylabel("Y")
#plt.savefig('pic.png')

x = np.linspace(0, np.pi * 10, 500)
fig, axes = plt.subplots(2, 1) # 2 graphs figures
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))
#fig.savefig("sin&cos.png")
