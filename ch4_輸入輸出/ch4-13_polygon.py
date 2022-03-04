import math

n=eval(input("請輸入N邊形: "))
s=eval(input("請輸入邊長: "))

area=(n*s**2)/(4*math.tan(math.pi/n))

print("面積 = ",area)