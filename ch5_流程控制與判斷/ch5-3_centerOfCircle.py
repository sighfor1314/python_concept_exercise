x,y = eval(input("輸入座標(請用,分開):"))

if((((abs(x-0)**2)+(abs(y-0)**2)))**0.5>20):   
   print("(%d,%d)不在圓內部"%(x,y))
else:
    print("(%d,%d)在圓內部"%(x,y))
