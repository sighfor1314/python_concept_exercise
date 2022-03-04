# ch9_24.py
armys = []                      # 建立小兵空串列
# 建立50個小兵
for soldier_number in range(50):
    soldier = {'tag':'red', 'score':3, 'speed':'slow'}
    armys.append(soldier)
# 列印前3個小兵
print("前3名小兵資料")
for soldier in armys[:3]:
    print(soldier)

for soldier in armys[-3:]:
    if soldier['tag'] == 'red':
        soldier['tag'] = 'green'
        soldier['score'] = 10
        soldier['speed'] = 'fast'
# 列印編號35到40的小兵
print("列印編號35到50小兵資料")
for soldier in armys[34:50]:
    print(soldier)
    
