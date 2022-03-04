a,b,c=eval(input("請輸入方程式係數:"))
temp=b**2-4*a*c
result1=((-b+(temp)**0.5))/2*a
result2=((-b+(temp)**0.5))/2*a
if(temp>0):
    print("有兩個實數根")
    print("結果為%f和%f"%(result1,result2))

elif(temp==0):
    print("有一個實數根")
    print("結果為%d"%result1)


else:
    print("沒有實數根")

