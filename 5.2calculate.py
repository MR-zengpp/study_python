import numpy as np 
x = [64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y = [62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
sum1 = np.mean(x)
sum2 = np.mean(y)
sum3 = sum4 = 0
for m in range(np.size(x)):
    sum3 += (x[m]-sum1)*(y[m]-sum2)
    sum4 += (x[m]-sum1)*(x[m]-sum1)
w = sum3/sum4
b=sum2-w*sum1
print("W=",w,"b=",b)

