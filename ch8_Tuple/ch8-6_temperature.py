maxTemperature=(30,28,29,31,33,35,32)
minTemperature=(20,21,19,22,23,24,20)

print("最高溫:",max(maxTemperature))
print("最低溫:",min(minTemperature))
print("平均溫度:",((sum(maxTemperature)/len(maxTemperature))+(sum(minTemperature)/len(minTemperature)))/2)