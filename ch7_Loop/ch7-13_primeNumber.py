nums=[]

for i in range(1,21):
    ans=0
    for j in range(2,i):
        if i%j==0:
            ans=1
            break
    if ans==0:
        nums.append(i)
print(nums)            