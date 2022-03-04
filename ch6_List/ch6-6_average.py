sc=[['洪錦魁',80,95,88,0],['洪冰儒',98,98,96,0],['洪雨星',90,91,92,0],['洪冰雨',91,93,95,0],['洪星宇',92,97,90,0]]
print(sc)
sc[0][4]=sum(sc[0][1:4])
sc[0].append(round(sc[0][4]/3,1))
sc[1][4]=sum(sc[1][1:4])
sc[1].append(round(sc[1][4]/3,1))
sc[2][4]=sum(sc[2][1:4])
sc[2].append(round(sc[2][4]/3,1))
sc[3][4]=sum(sc[3][1:4])
sc[3].append(round(sc[3][4]/3,1))
sc[4][4]=sum(sc[4][1:4])
sc[4].append(round(sc[4][4]/3,1))

print(sc)