# Python Classes

class Test:
      name = 'I am the class'
      def printName(self, age):
          print('i am a method of the class')
          print(age)

x = Test()

x.printName(80)

# NB: make double the underscoring
class Test2:
     def __init__(self, name):
         self.name = name
         print('I am the init function')
    
y = Test2('y') 
print(y.name)
x = Test2('x')
print(x.name)
    

class Dog:

    scientific__name = 'canis'

    def __init__(self, name):
        self.name = name 

duke = Dog('duke')
bob = Dog('bob')

print(duke.scientific__name)
print(duke.name)

print(bob.scientific__name)
print(bob.name)


class Hero:
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def eating(self, food):
        if food =='pasta':
            self.energy = self.energy + 10
        elif food == 'pizza':
            self.energy = self.energy - 20


# mario = Hero('Mario')
# addisu = Hero('Addisu')

# print(mario.name)
# print(mario.energy)
# mario.eating('pasta')
# mario.eating('pizza')
# print(addisu.name)
# print(addisu.energy)

class BaseClass:
    def printName(self):
        print('I come from the Base Class')
class SubClass(BaseClass):
    pass

a = SubClass()
a.printName()



class Employee:
    def __init__(self, name, paycheck):
        self.name = name
        self.paycheck = paycheck

    def raise__paycheck(self,number):
        self.paycheck = self.paycheck+(self.paycheck*number)

mario = Employee('Mario', 1000)
print(mario.name)
print(mario.paycheck)

mario.raise__paycheck(0.1)
print(mario.paycheck)








