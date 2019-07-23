# To inherit a class, put super class name in parenthesis of the class

class Wolf:
    def __init__(self,name,color):
        self.name = name
        self.color= color
    def bark(self):
        print("OOOOOO")

class Dog(Wolf):
    def bark(self):
        print("bowww")
        super().bark()


fles = Dog("ginger","black")
fles.bark()

# super method is use to call the methods of the super class
