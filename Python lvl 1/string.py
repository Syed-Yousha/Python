
# \\\\\\\\\\\\\\\\\\ String

# "Hello" 0r 'Hello' string value will always be in quotations
string = "Elephant"


#\\\\\\\\ Printing
print("---------- Printing------------")
print(string)


#\\\\\\\\ Indexing
print("---------- Indexing------------")
print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])


#\\\\\\\\\\\ Slicing
print("---------- Slicing------------")
print(string[1:]) #output will be from 2nd index to last value
print(string[:3]) #output will start from 0th index to 2nd index (not including index 3)
print(string[:]) # it means print all value from start to end
print(string[::1]) # this mean print every value in step of 1
print(string[::2]) # this mean print every value in step of 1


#\\\\\\\\\\\ Basic Methods
print("---------- Basic Methods ------------")
x = string.upper() # Will turn all letters to uppercase
print(x)

x = string.lower() # Will turn all letters to lowercase
print(x)

x  = string.capitalize() # Will turn first character uppercase
print(x)


string = "Hello World"
x = string.split() # Will split both words
print(x)


x = string.split('e') # Will make 'e' the spliter or split mirror
print(x)


x = string.split('o') # Will make 'o' the spliter
print(x)



#\\\\\\\\\\\ Printing format
print("---------- Printing format ------------")

x = "Insert another string here: {}".format("Insert Me!") #Value in .format() bracket will get into {} curly bracket
print(x)


x = "item one: {}, Item two: {}".format("dog", "cat" ) #Value one will get into {bracket} one and value two will get into {bracket} two
print(x)


x = "item one: {x}, Item two: {y}".format( x= "dog", y= "cat" ) # value of variable will be printed where we put variable
print(x)


x = "item one: {y}, Item two: {x}".format( x= "dog", y= "cat" )
print(x)





x = "item one: {x}, Item two: {x}".format( x= "dog", y= "cat" )
print(x)

a = 'dog'
b = 'cat'
x = f"item one: {a} , item two: {b}"
print(x)