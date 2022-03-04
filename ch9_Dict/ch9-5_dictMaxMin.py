noodles = {'牛肉麵':100, '肉絲麵':80, '陽春麵':60,
           '大滷麵':90, '麻醬麵':70}

noodle=noodles.items()
print(type(noodle))

print(max(noodle,key=lambda item:item[1]))
print(min(noodle,key=lambda item:item[1]))


    


