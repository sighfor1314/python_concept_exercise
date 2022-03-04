fruits={'Watermelon':15,'Banana':20,'Pineapple':25,'Orange':12,'Apple':18}
print(fruits)
fruit=sorted(fruits.items(),key=lambda item:item[0])
print(fruit)
