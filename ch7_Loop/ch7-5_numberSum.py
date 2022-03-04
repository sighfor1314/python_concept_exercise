n,m=eval(input("請輸入n,m:"))
total=0
if n>m:
    n,m=m,n
for i in range(n,m+1):
    total+=i
print(total)