import math


print("-" * 40)
print(" "*8+"一元二次方程求解 ax²+bx+c")
print("-" * 40)

a = float(input("请输入a的值:"))
b = float(input("请输入b的值:"))
c = float(input("请输入c的值:"))
print("该一元二次方程为%.2fx²+%.2fx+%.2f"%(a,b,c))
m=b**2-4*a*c
x1=0
x2=0
if m > 0:
    x1 = (math.sqrt(m)-b)/2
    x2 = (-math.sqrt(m)-b)/2
    print("该方程有两个不同的解，两个解分别是%.2f,%.2f"%(x1,x2))
elif m == 0:
    x1 = (math.sqrt(m)-b)/2
    print("该方程有两个相同的解，该解是%.2f"%(x1))
else:
    print("该方程没有解")


