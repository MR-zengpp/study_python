import tensorflow as tf 
x1 = tf.constant([137.97,104.50,100.00,124.32,79.20,99.00,124.00,114.00,106.69,
138.05,53.75,46.91,68.00,63.02,81.26,86.21])
x2 = tf.constant([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2],dtype=tf.float32)
x2 = tf.cast(x2,dtype=tf.float32)
y = tf.constant([145.00,110.00,93.00,116.00,65.32,104.00,118.00,91.00,
62.00,133.00,51.00,45.00,78.50,69.65,75.69,95.30])

x0 =tf.ones(len(x1))
X = tf.stack((x0,x1,x2),axis=1)
Y =tf.reshape(y,[-1,1])

Xt = tf.transpose(X)
XtX_1 = tf.linalg.inv(tf.matmul(Xt,X))
XtX_1_Xt = tf.matmul(XtX_1,Xt)
W = tf.matmul(XtX_1_Xt,Y)
W = tf.reshape(W,[-1])

print("多元线性回归方程:")
print("Y=",W[1].numpy(),"*x1+",W[2].numpy(),"*x2+",W[0].numpy())

print("请输入房屋面积和房间数，预测房屋销售价格:")
x1_test = float(input("商品房面积:"))
x2_test = int(input("房间数:"))

y_pred = W[1].numpy()*x1_test+W[2].numpy()*x2_test+W[0].numpy()
print("预测价格:",round(y_pred,2),"万元")