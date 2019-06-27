## exception handling in files using try and except clause
##Common exceptions:
##ImportError: an import fails;
##IndexError: a list is indexed with an out-of-range number;
##NameError: an unknown variable is used;
##SyntaxError: the code can't be parsed properly;
##TypeError: a function is called on a value of an inappropriate type;
##ValueError: a function is called on a value of the correct type, but with an inappropriate value.


# On try statement can have multiple select blocks
try:
   variable = 10
   #print(variable + "hello")
   print(variable / 0)
except ZeroDivisionError:
   print("Divided by zero")
except (ValueError, TypeError):
   print("Error occurred")


# Empty except clause will cache all the exceptions
try:
    variable =10
    print(10/0)
except:
    print("Error occured")
finally:
    print("Yeah!!!")


### Finally clause runs no matter exception occurs for not

# raise clause to throw an exception

a = -1
if a<0:
    raise ValueError("Negative number!!")

## you can  raise a same error within Except clause

try:
    b = 10
    print(10/0)
except ZeroDivisionError:
    raise



