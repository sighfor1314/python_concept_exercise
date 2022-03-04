tempType=(input("請輸入攝氏f或華氏c:"))
if(tempType=='f'):
    c=eval(input("請輸入攝氏溫度:"))
    f=int(c)*(9/5)+32
    print("攝氏%d度 = 華氏 %d 度"%(c,f))
if(tempType=='c'):
    f=input("請輸入華氏溫度:")
    c=(int(f)-32)*5/9
    print("攝氏%s度 = 華氏 %4.1f"%(c,f))