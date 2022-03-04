
distance=384400
speed=1225
hour,minute=divmod(distance,1225)
#print("minute="+str(minute))
#hour,minute=divmod(minute,60)
day,hour=divmod(hour,24)
minute,second=divmod(minute,60)
print("day = "+str(day)+'\t'+"hour = "+str(hour)+'\t'+"minute = "+str(minute)+'\t'+"second = "+str(second))
