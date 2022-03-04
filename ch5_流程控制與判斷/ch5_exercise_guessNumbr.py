ans=0
print("猜數字遊戲,請心中想一個0-7之間的數字,然後回答問題")
truefalse="請輸入y或Y代表有,其他代表無"
q1="有沒有看到心中的數字:1,3,5,7"
num=input(q1+truefalse)
if(num=='y'or num=="Y"):
    ans+=1
q2="有沒有看到心中的數字:2,3,6,7"    
num=input(q2+truefalse)
if(num=='y'or num=="Y"):
    ans+=2
q3="有沒有看到心中的數字:4,5,6,7"  
num=input(q3+truefalse)
if(num=='y'or num=="Y"):
    ans+=4

print("心中的數字為%d"%ans)


