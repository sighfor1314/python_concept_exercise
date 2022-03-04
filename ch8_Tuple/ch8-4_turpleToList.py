tp=[1,2,3,4,5,2,3,1,4]
tp_list=list(tp)
for wd in tp_list:
    if tp_list.count(wd)>1:
        tp_list.remove(wd)#刪除1次出現
print(tp_list)         
newtp=tuple(tp_list)
print(newtp) 