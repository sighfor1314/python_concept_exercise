files = ['da1.jpg','da2.png','da3.gif','da4.gif','da5.jpg','da6.jpg','da7.gif']
jpg=[]
png=[]
gif=[]
for file in files:
    if file.endswith('.jpg'):
        jpg.append(file)
    elif file.endswith('.png'):
        png.append(file)
    else:
        gif.append(file)
print (jpg,png,gif)     

