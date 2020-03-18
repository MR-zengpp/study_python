import matplotlib.pyplot as plt 
import numpy as np 
import tensorflow as tf 

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_, _) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif']="SimHei"
plt.rcParams['axes.unicode_minus']=False

titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE",
        "DIS","RAD","TAX","PTRATIO","B","LSTAT"]
fig1 = plt.figure('fig1',figsize=(9,9)) 
for i in range(13):
    plt.subplot(4,4,(i+1))
    plt.scatter(train_x[:,i],train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1)+"."+titles[i]+" - Price")   

plt.tight_layout(rect=[0,0,1,0.9])
plt.suptitle("各个属性与房价的关系",fontsize=20)
plt.show()

fig2 = plt.figure('fig2') 
print('''
      "1 -- CRIM",
      "2 -- ZN",
      "3 -- INDUS",
      "4 -- CHAS",
      "5 -- NOX",
      "6 -- RM",
      "7 -- AGE",
      "8 -- DIS",
      "9 -- RAD",
      "10 -- TAX",
      "11 -- PTRATIO",
      "12 -- B",
      "13 -- LSTAT"
      ''')
m = int(input("请选择属性:"))
plt.subplot()
plt.scatter(train_x[:,m-1],train_y)
plt.xlabel(titles[m-1])
plt.ylabel("Price($1000's)")
plt.title(str(m)+"."+titles[m-1]+" - Price") 
plt.show()

