nums=[]

for i in range(1,21):
    for j in range(2,i):
        if i%j==0:
            break
    else :
        nums.append(i)
print(nums)            