class Person:
    def __init__(self,name):
        self.name = name

    def say_hello(self):
        print('hello ,how are you',self.name)

p = Person('swaroop')

p.say_hello()

