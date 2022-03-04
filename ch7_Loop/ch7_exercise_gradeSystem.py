sc=[[1,'洪錦魁',80,95,88,0],[2,'洪冰儒',98,98,96,0],[3,'洪雨星',90,91,92,0],[4,'洪冰雨',91,93,95,0],[5,'洪星宇',92,97,90,0]]
#print(sc)
for i in range(len(sc)):
    sc[i][5]=sum(sc[i][2:5])
    sc[i].append((round(sc[i][5]/3,1)))
print("原始成績'\n'",sc)
sc.sort(key=lambda x:x[5],reverse=True)
for i in range(len(sc)):
    sc[i].append(i+1)
    if sc[i][5]==sc[i-1][5]:
        sc[i][7]=sc[i-1][7]
      
print("填入名次'\n'",sc)
sc.sort(key=lambda x:x[0])
print("最終成績單'\n'",sc)

