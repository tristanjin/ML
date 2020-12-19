'''
Created on 2020. 12. 1.

@author: Tristan Jin
'''
import tensorflow.compat.v1 as tf
import numpy as np
from pandas.io.parsers import read_csv
from numpy import float32

tf.compat.v1.disable_eager_execution()

model = tf.global_variables_initializer()

data = read_csv('price data.csv', sep=',')

xy = np.array(data, dtype=np.float32)

# x 는 1 부터 4까지, y는 5 번째
'''
year    avgTemp    minTemp    maxTemp    rainFall    avgPrice
20100101    -4.9    -11    0.9    0    2123
20100102    -3.1    -5.5    5.5    0.8    2123
20100103    -2.9    -6.9    1.4    0    2123
20100104    -1.8    -5.1    2.2    5.9    2020
20100105    -5.2    -8.7    -1.8    0.7    2060
20100106    -7.3    -11.4    -2.5    0.3    2060
20100107    -6.7    -11.2    -1.2    0    2140
20100108    -5.6    -11.4    1.4    0    2140
20100109    -3.1    -8.8    1.8    0.1    2140

'''
x_data = xy[:, 1:-1]
y_data = xy[:, [-1]]
'''
placeholder 에  4개의  값이 담길수 있도록 설정
'''
X = tf.placeholder(tf.float32, shape=[None, 4])
Y = tf.placeholder(tf.float32, shape=[None, 1])

W = tf.Variable(tf.random_normal([4,1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = tf.matmul(X, W) + b

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000005)

train = optimizer.minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for step in range(100001):
    cost_, hypo_, _ = sess.run([cost,hypothesis,train], feed_dict={X: x_data, Y: y_data})
    if step % 500 ==0:
        print("#",step, "손실 비용: ", cost_)
        print("배추가격", hypo_[0])

"모델 저장 - 가장 기본적인 saver 이용"
saver = tf.train.Saver()

save_path = saver.save(sess, "./saved.cpkt")