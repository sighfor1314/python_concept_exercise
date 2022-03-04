fs=open("d:4.txt",mode="w")

print("姓名   國文   英文   總分",file=fs)
print("%3s   %4d   %4d   %4.1f" %("洪冰儒",98,90,188.1),file=fs)
print("%3s   %4d   %4d   %4.1f" %("洪雨星",96,95,191.0),file=fs)
print("%3s   %4d   %4d   %4.1f" %("洪冰雨",92,88,180.0),file=fs)
print("%3s   %4d   %4d   %4.1f" %("洪星雨",93,97,190.0),file=fs)

fs.close()