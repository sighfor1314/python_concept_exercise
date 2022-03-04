people=(1100,652,946,821,955,1024)
average=sum(people)/len(people)
print(average)
var=0
for n in people:
    var+=(n-average)**2
var/=(len(people)-1)    
print("變異數:",var)

dev= var**0.5
print("標準差:",dev)

