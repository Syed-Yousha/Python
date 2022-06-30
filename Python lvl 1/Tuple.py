# \\\\\\\\\\\\\\\\\BOOLEAN
print('\\\\\\\\\\\\\\BO0LEAN')

func = True
print(func)

func = False
print(func)

#\\\\\\\\\\\\\ TUPLES
print('\\\\\\\\\\\\\ TUPLES')
tup = (1, 2, 3)
print(tup)
print(tup[0])
# tup[0] = 'new': Tuples can not be assigned to another value they're immutable
tup = (1, 'new', True)
print(tup) # tuples supports all data types


print('\\\\\\\\\\\ List can be re-assigned')
my_list = [1,2,3,4]
print(my_list)

my_list[0] = 'New'
print(my_list)


#\\\\\\\\\\\\\\\\ SETS
print('\\\\\\\\\\\\\\\\ SETS')

x = set()
x.add(1)
x.add(2)
x.add(4)
x.add(3)
x.add(3)
x.add(3)
x.add('hello')
print(x) # Set {} only consider unique item means it will take one value on time only (means 3 will be printed only one time)

coverted = set([1,2,2,2,3,3,3,2,4])
print(coverted)
my_set = {1, 2, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2}
print(my_set)


