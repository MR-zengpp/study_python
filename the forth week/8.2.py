import tensorflow as tf 
import numpy as np 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
x=tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y=tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])

sum1 = sum2 = sum3 = sum4 = sum5 = w = b =0
sum2 = tf.reduce_sum(x) * tf.reduce_sum(y)
for i in range(tf.size(x)):
    sum1 += x[i] * y[i]
    sum3 += tf.square(x[i])
    sum4 = tf.square(tf.reduce_sum(x))

sum5 = tf.cast(tf.size(x),dtype = tf.float32)
w = (sum5 * sum1 - sum2) / (sum5 * sum3 - sum4) 
b = (tf.reduce_sum(y) - w * tf.reduce_sum(x) ) /sum5
print("W=",w,"\nb=",b)



