buyers=[['Jame',1030],['Curry',893],['Durant',2050],['Jordan',990],['David',2110],['Kevin',15000],['Mary',10050],['Tom',8800]]
infinitebuyers=[]
vipbuyers=[]
goldbuyers=[]
for buyer in buyers:
    if buyer[1]>=10000:
        infinitebuyers.append(buyer)
    elif buyer[1]>=1000:
        vipbuyers.append(buyer)
    else:
        goldbuyers.append(buyer)

print("infinitebuyers:",infinitebuyers,'vipbuyers:',vipbuyers,'goldbuyers:',goldbuyers)