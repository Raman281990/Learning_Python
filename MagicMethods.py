# Special methods that have double underscore at the beginning and the end of the method
# called Dunders(used for operator overloading)
# __sub__
# __mul__

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)


first = Vector2D(2,4)
second = Vector2D(5,10)
result = first+second
print(result.x)