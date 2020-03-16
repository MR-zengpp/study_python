import numpy as np 
np.random.seed(612)
a = np.random.rand(1000)
i = int(input("请输入一个1-100之间的整数:"))
n = 1
if i < 1 or i > 100:
    print("输入不规范！")
else:
    for m in range(1000):            
        if m % i == 0:            
            print("序号\t索引值\t随机数" )
            print(n,"\t",m,"\t",a[m])
            n+=1