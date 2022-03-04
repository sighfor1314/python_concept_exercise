class Myschool():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def msg(self):
        return self.name.title()
myschool=Myschool('kevin',80)        
print(myschool.msg())
print(myschool.score)

        
