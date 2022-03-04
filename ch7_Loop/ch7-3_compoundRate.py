money =50000 #本金
rate=0.015 #利率
year=5
total=50000
for i in range(year):   
    total *= (1+rate)
    print('本金 = ',money,'利率 = ',rate,'存款年數 = ',i,'money=',total)

