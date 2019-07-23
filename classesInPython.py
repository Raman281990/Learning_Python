class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs

    def bark(self):
        print("boww!!")

flex = Cat("ginger", 4)
print(flex.color)
flex.bark()

# classes can have other
# trying to access the attribute of class that is not defined causes AttributeError

#flex.width