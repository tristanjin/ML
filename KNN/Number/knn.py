'''
Created on 2020. 12. 7.

@author: Tristan Jin
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32)
response = np.random.randint(0, 2, (25, 1)).astype(np.float32)

red =trainData[response.ravel() == 0]
blue = trainData[response.ravel() == 1]

plt.scatter(red[:,0], red[:, 1], 80, 'r', '^')
plt.scatter(blue[:,0], blue[:, 1], 80, 'b', 's')

newcomer = np.random.randint(0,100, (1,2)).astype(np.float32)
plt.scatter(newcomer[:,0], newcomer[:,1], 80, 'g', 'o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, response)
ret, results, neighbours, dist = knn.findNearest(newcomer, 3)

print("result : ", ret)
print("neighbours:", neighbours)
print("distance: ", dist)

plt.show()