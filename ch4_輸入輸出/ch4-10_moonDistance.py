distance=384400
speed=eval(input("請輸入馬赫數(公里/小時): "))

hour,minute=divmod(distance,speed)

day,hour=divmod(hour,24)
print("day = "+str(day)+'\t'+"hour = "+str(hour)+'\t'+"minute = "+str(minute))

s