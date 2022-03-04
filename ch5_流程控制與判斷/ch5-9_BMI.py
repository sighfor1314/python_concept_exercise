height,weight=eval(input("請輸入身高及體重:"))
bmi=weight/((height/100)**2)
if(bmi<18.5):
    print("%f體重過輕"%bmi)
elif(bmi<24):
    print("%f體重正常"%bmi)
elif(bmi<28):
    print("%f體重超重"%bmi)
else:
    print("%f體重肥胖"%bmi)

