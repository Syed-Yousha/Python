# \\\\\\\\ Dictionaries
print("\\\\\\\\\\\\\\\\\\\\ Dictionaries ")

my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict['key1'])


# we have to print grabMe only
my_dict = {'key1':123, 'key2':'value2', 'key3':{'123':[1,2,'grabMe']}}
print(my_dict)
print(my_dict ['key3']['123'][2] )

#//////////// ReValue a dictionary
print('//////////// ReValue a dictionary')


my_dict = {'lunch': 'pizza', 'bfast':'eggs' }
print(my_dict['lunch'])

my_dict['lunch'] = 'Zinger Cheese Burger'
my_dict['dinner'] = 'Pasta'

print(my_dict['lunch'])
print(my_dict)

