
num1 = input("輸入三個值:")
num2 = input("輸入三個值:")
num3 = input("輸入三個值:")

if(num1>num2):
    if(num1>num3):
        print (num1)
        if(num2>num3):
            print (num2+'\n'+num3)
        else:
            print (num3+'\n'+num2)
    else:
        print (num3+'\n'+num1+'\n'+num2)
else:
    if(num2>num3):
        print (num2)
        if(num3>num1):
             print (num3+'\n'+num1)
        else:
            print (num1+'\n'+num3)     
    else:
         print (num3+'\n'+num2+'\n'+num1)    

      


