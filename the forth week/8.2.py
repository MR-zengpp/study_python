import tensorflow as tf 
import numpy as np 


x=tf.constant([ 64.3, 99.6, 145.45, 63.75, 135.46, 92.85, 86.97, 144.76, 59.3, 116.03])
y=tf.constant([ 62.55, 82.42, 132.62, 73.31, 131.05, 86.57, 85.49, 127.44, 55.25, 104.84])


sumXY = tf.reduce_sum(x*y)
sumX_Y = tf.reduce_sum(x)*tf.reduce_sum(y)
sumX_2 = tf.reduce_sum(tf.square(x))
sumX2 = tf.square((tf.reduce_sum(x)))
w = (len(x)*sumXY - sumX_Y) / (len(x)*sumX_2-sumX2) 
b = (tf.reduce_sum(y)-w*tf.reduce_sum(x))/len(x)
print("W=",w.numpy(),"\nb=",b.numpy())





