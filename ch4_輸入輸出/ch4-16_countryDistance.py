import math

R=6371 #地球半徑
x1,y1= 39.9196,116.3669 #北京故宮博物館經緯度
x2,y2=48.8595,2.3369 #法國巴黎羅浮宮經位度

d=R*math.acos(math.sin(math.radians(x1))*math.sin(math.radians(x2))+math.cos(math.radians(x1))*math.cos(math.radians(x2))*math.cos(math.radians(y1-y2)))

print("distance = ",d," 公里")