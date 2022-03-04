month={'一月':'January','二月':'February','三月':'March','四月':'April','五月':'May','六月':'June',
'七月':'July','八月':'August','九月':'September','十月':'October','十一月':'November','十二月':'December'}

x=input("請輸入中文月份:")
if x in month:
    print(month[x])
else:
    print("查無資料")