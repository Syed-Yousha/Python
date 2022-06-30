# LEGB

# Local
# Enclosing function locals
# Global
# Built-in level

x = 25  # Global scope, this can be accessed throughout the code.

def my_func():
    x = 50  # Enclosing function locals, only accessed in scope of function.
    return x

print(x)
print(my_func())

# \\\\\\\\\\\\\\\\\ Lambda function
print('\\\\\\\\\\ Lambda function')
add = lambda a: a + a + a + 15  # lambda is a function we can make in a variable
print(add(10))


# Enclosing function local example.
print('\\\\\\\\\\\  Enclosing function local example')

name = "this is a glaboal name!"

def greet():
    name = "sammy"

    def hello():
        print("hello "+name)

    hello()

greet()
print(name)


# Global Variable
print('\\\\\\\\\ Global Variable')

x = 50

def func():
    global x # this global function will globally change the variable value through a function
    x = 1000


print("before function call, x is: ", x)
func()
print("before function call, x is: ", x)