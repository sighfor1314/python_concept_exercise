a,b,e,c,d,f=eval(input("請輸入方程式係數:"))
temp=a*d-b*c
result1=(e*d-b*f)/(a*d-b*c)
result2=(a*f-e*c)/(a*d-b*c)
if(temp==0):
    print("此方程式無解")
else:
    print("x=%f,y=%f"%(result1,result2))

