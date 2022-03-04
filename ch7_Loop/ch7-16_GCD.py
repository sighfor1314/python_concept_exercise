x,y=eval(input("輸入兩個數字:"))
gcd=[]
if x>y:
    x,y=y,x
for i in range(1,x+1):
    if x%i==0 and y%i==0:
        gcd.append(i)
print(max(gcd))        