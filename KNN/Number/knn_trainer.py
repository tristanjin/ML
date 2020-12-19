'''
Created on 2020. 12. 13.

@author: Tristan Jin
'''
import os 
import cv2
import numpy as np

files_names = list(range(0,13))
train = []
train_labels = []

# ('./training_data/0/', [], ['1.png', '2.png', '3.png', '4.png'])

for file_name in files_names:
    path = './training_data/'+str(file_name)+"/"
    file_count = len(next(os.walk(path))[2])
#    print("os.walk[0]: " , list(os.walk(path))[0])
    for i in range(1, file_count+1):
        img = cv2.imread(path+str(i)+".png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        train.append(gray)
        train_labels.append(file_name)
        print(file_name)

x = np.array(train)
train = x[:,:].reshape(-1, 400).astype(np.float32)
train_labels = np.array(train_labels)[:,np.newaxis]
np.savez("trained.npz", train=train, train_labels=train_labels)