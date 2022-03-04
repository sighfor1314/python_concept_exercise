abc="Are you sleeping,are you sleeping,Brother John,Brother John?Morning bells are ringing,morning bells are ringing.Ding ding dong,ding ding dong"
str1=abc.replace(','," ")
str1=str1.replace('?'," ")
str1=str1.replace('.'," ")
print(str1)
print(len(str1))
x=list(str1.split(" "))
print(x)

str2=input("輸入字串:")
print(str1.count(str2))
