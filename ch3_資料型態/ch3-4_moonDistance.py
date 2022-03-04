distance=384400
speed=250

minute=int(distance/speed)
#print("minute="+str(minute))
hour,minute=divmod(minute,60)
day,hour=divmod(hour,24)
print("day = "+str(day)+'\t'+"hour = "+str(hour)+'\t'+"minute = "+str(minute))
