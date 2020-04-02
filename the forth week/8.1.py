import tensorflow as tf 
x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
x_ = tf.reduce_mean(x)
y_ = tf.reduce_mean(y)
sum1 = sum2 = w = 0
for i in range(tf.size(x)):
   sum1 +=  (x[i] - x_) * (y[i] - y_)
   sum2 +=tf.square((x[i] - x_))
w = sum1 / sum2
b = y_- w * x_
print("W=",w,"\nb=",b)