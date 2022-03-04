money =100000 #本金
rate=(eval(input("請輸入年利率: ")))*0.01
year=eval(input("請輸入存款年數: "))
total = money*(1+rate)**year
print("money= %d "%total)

