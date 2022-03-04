import math

R=6371 #地球半徑
x1,y1=eval(input("請輸入經緯度")) #北京故宮博物館經緯度
x2,y2=eval(input("請輸入經緯度")) #法國巴黎羅浮宮經位度

d=R*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1-y2)))

print("distance = ",d," 公里")