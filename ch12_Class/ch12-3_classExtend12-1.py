class Myschool():
    def __init__(self):
        self.name='python school'
    def department(self):
        depart=['機械','電機','資工']
        return depart
    def msg(self):
        
        return 'title:'

myschool=Myschool()   
     
print(myschool.msg())
print(myschool.name.title())
print(myschool.department())

        
