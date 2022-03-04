euler=1
e=1
for i in range(1,101):
    e*=i
    euler+=1/e
    if i%10==0:
        print(euler)      


   
    
