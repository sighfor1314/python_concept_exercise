x,y,z=eval(input("請三個邊長:"))

if(x+y>z):
    print("周長為:%d"%(x+y+z))
else:
    print("這不是三角形邊長")
