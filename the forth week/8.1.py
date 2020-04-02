import tensorflow as tf 
import numpy as np 
x = tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_ = tf.reduce_mean(x)
y_ = tf.reduce_mean(y)

sum1 = tf.reduce_sum( (x-x_) * (y - y_))
sum2 =tf.reduce_sum((x-x_)*(x-x_))
w = sum1 / sum2
b = y_- w * x_
print("W=",w.numpy(),"\nb=",b.numpy())
