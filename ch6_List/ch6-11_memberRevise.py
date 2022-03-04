member=['Mary','Josh','Tracy']
print(member)
num=eval(input("輸入1新增,輸入2刪除:"))
str1=(input("name:"))
if(num==1):
    member.append(str1)
    print(member)
elif(num==2):
    if str1 in member:
        member.remove(str1)
        print(member)
    else:
        print("名單輸入錯誤")    
