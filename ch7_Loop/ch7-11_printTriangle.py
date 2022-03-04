for i in range(1,10):
    for k in range(10-i,0,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print(i-k+1,end="")    
    for j in range(1,i+1):
        print(j,end="")
    print()
    