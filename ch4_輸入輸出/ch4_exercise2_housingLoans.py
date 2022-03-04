loan=eval(input("輸入貸款金額: "))
year=eval(input("輸入貸款年限: "))
rate=eval(input("輸入貸款年利率: "))

monthRate=rate/12*0.01
molecules=loan*monthRate   #分子 貸款金額*月利率
denominator=1-1/((1+monthRate)**(year*12)) #分母     1-(1/(1+月利率)**(貸款年限*12))
monthlyPay=molecules/denominator #每個月還款金額
totalPay=monthlyPay*12*year #總共還款金額

print("每個月還款金額 %d",int(monthlyPay))  #float轉int
print("總共還款金額 %d",int(totalPay))   