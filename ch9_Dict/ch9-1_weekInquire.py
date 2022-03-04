week={'Sunday':"星期日",
    'Monday':'星期一',
    'Tuesday':'星期二',
    'Wendesday':'星期三',
    'Tursday':'星期四',
    'Friday':'星期五',
    'Saturday':'星期六'}
wd=input("請輸入查詢的單字:")
str1=wd.title()
if str1 in week:
    print(str1,"中文意思:",week[str1])
else:
    print('查無此單字')   