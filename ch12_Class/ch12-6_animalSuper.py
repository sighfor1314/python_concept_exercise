class Animal():
    def __init__(self,animal_name,animal_age):
        self.name=animal_name
        self.age=animal_age
    def run(self):
        print(self.name.title(),'is running')
class Dog(Animal):
    def __init__(self,dog_name,dog_age):
        super().__init__(dog_name,dog_age)
    def sleeping(self):
        print(self.name.title(),'is sleeping')

class Birds(Animal):
    def __init__(self,birds_name,birds_age):
        super().__init__(birds_name,birds_age)
    def flying(self):
        print(self.name.title(),'is flying')


mycat=Animal('lucy',6)
mydog=Dog('pipi',12)
mybirds=Birds('papa',2)
print(mycat.name.title(),'is',mycat.age,' years old')
mycat.run()

print(mydog.name.title(),'is',mydog.age,' years old')
mydog.sleeping()
print(mybirds.name.title(),'is',mybirds.age,' years old')
mybirds.flying()
