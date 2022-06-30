

# \\\\\\\\\\\ Functions
print('\\\\\\\\\\\ Functions')

def my_func(param1 = 'default'):
    """
    This is the DOCSTRING ( Documentation String )

    This will be considered as comment, and we can write paras in it
    """
    print(f'My First Python Function, Parameter value = {param1}')


my_func()


# \\\\\\\\\ Returning
print('\\\\\\\\\ Returning')

def hello():
    """
    This function will return " Hello "
    """
    return "Hello"


result =  hello() #Hello function return value.So, we can store it in a Variable
print(result)



#\\\\\\\\\ Parameter Function
print('\\\\\\\\ Parameter Function')
def add_num(num1,num2):
    if type(num1)== type(num2) == type(10):
        return num1 + num2
    else:
        return "We need integers"

result = add_num(2,3) #Python can also add string,So, beware of types
print(result)




# \\\\\\\\\Lambda expression
print('\\\\\\\\\\\ Lambda expression')
my_list = [1, 2, 3, 4, 5, 6, 7, 8]

def even_bool(num):
    return num%2 == 0  # This statement return true if value is even and false if value is odd.

# x = even_bool(10)  # check if statement is working
# print(x)

# Filter
evens = filter(even_bool, my_list) # Filter function, it takes every value of sequence to the function and filter the list.

print('.....simple filter')
print(list(evens))


#\\\\\\\\\ Function as a Lambda expression
evens = filter(lambda num:num%2 == 0, my_list)
print('.....filter with lambda')
print(list(evens))


#\\\\\\\\\ String Operators
print('\\\\\\\ String Operators')

# Split
print('..... Split')

tweet = "Go sports! #Sports"
result = tweet.split('#')
print(result)
print(tweet.split('#')[1]) # For printing just the hashtag


# in Operator
print('.... In')

print('x' in [1,2,3,4] ) # if X is in the list then it will tell you in Boolean
print('x' in [1,2,3,4,'x'] )
