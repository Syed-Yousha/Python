#\\\\\\\\\\\\\ Strings
print('\\\\\\\\\\\\\ Strings')
my_string = 'django'

print(my_string[0])
print(my_string[-1])
print(my_string[:4])
print(my_string[1:4])
print(my_string[4:])
x = my_string[::-1]
print(x)

#\\\\\\\\\\\\\\\\ Lists
print('\\\\\\\\\\\\\\\\ Lists')
l = [3,7,[1,4,'hello']]
l[2][2] = "goodbye"
print(l)


#\\\\\\\\\\\\\ Dictionaries
print('\\\\\\\\\\\\\ Dictionaries')

d1 = {'simple_key' :'hello'}
d2 = {'k1' :{'k2': 'hello'}}
d3 = {'k1' :[{'nest_key' :['this is deep', ['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0] )


#\\\\\\\\\\\\\\\\ Sets
print('\\\\\\\\\\\\\\\\ Sets')
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(mylist)
my_dict = set(mylist)
print(my_dict)


#\\\\\\\\\\\\\\\\ Variables
print('\\\\\\\\\\\\\\\\ Variables')

age = 4
name = 'sammy'

print(f'"Hello my dog name is {name} and he is {age} years old "')
print("Hello my dog name is {a} and he is {b} years old ".format(a = name, b = age )) #this method is helpful when sometimes we have to re-arrange variables
