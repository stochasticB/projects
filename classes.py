# Object Orientated Programming in Python

class Goober:  #Goober
    def __init__(self, name):    # instantiate object right when it's created
        self.name = name    # these don't need to match in name
        print(name)

    def add_one(self, x):
        print(x + 1)

    def bark(self):         # 'self' - we need to invisibily pass the dog object through itself so that we know which dog we're accessing
        print("bark")

    def get_name(self):



d = Goober('Stella')  # instance of class Dog
print(d.name)   # name is now an attribute of the Goober
#   d.bark()
#d.add_one(5)

#print(type(d))  # <class '__main__.Dog'>; default module = __main__ is the module that this class is in.


class Chonk:
    def __init__(self, name):
        self.name = name
        print(name)

    def meow(self):
        print('Meow, meow, feed me!')

    def feed(self,x):
        print('The monthly food budget for this chonk is $:', x)



s = Chonk("Smelly")
#Smelly.meow()
#Smelly.feed(15)
