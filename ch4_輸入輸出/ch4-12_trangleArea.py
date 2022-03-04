x1,y1,x2,y2,x3,y3=eval(input("請輸入三點座標: "))
dist1=((x1-x2)**2+(y1-y2)**2)**0.5
dist2=((x2-x3)**2+(y2-y3)**2)**0.5
dist3=((x3-x1)**2+(y3-y1)**2)**0.5
p=(dist1+dist2+dist3)/2

area=(p*(p-dist1)*(p-dist2)*(p-dist3))**0.5

print("三角形面積為 = %.2f" %area)
