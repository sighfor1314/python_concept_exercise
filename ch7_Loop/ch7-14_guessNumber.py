answer=87
guess=0
count=0
while guess!=answer:
    guess=eval(input("請猜1-100:"))
    if guess>answer:
        count+=1
        print("less")
    elif guess<answer:
        count+=1
        print("large")
    else:
        print("答對了,共猜了%d次"%(count+1))