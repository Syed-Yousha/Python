# # \\\\\\\\\\ NOTES
#
# # Greater than
# 2 > 1
#
# # Less than
# 1 < 2
#
# # Greater than  or equal to
# 3 >= 2
#
#
# # Less than or equal to
# 1 <= 3
#
# # Equality
# 1 == 1  # True, '==' use for checking data type and value
# 1 == '1'  # False, they're data type ain't equal
# 'hi' == 'bye' # False, they're value isn't equal (there is no triple equals to sign in Python)
#
#
# # Inequality
# 1 != 2 #True, not equals to
# 1 != 1 #False
# 1 != 'Hi' #True


## Logical operator
#
# # AND
# (2 > 1 ) and ( 8 > 3) # program will run if both conditions are true
#
# # OR
# (2 > 1 ) or ( 8 > 3) # program will run if any conditions is true
#
#
# # Multiple Logical operator
# (1 > 0) or (2 > 1) or (3 > 2)


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ REAL DEAL BEGINS \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# If Statement
print('\\\\\\\ If Statement')

if 5 > 2 :
    print('First Block')
    if 2 < 10 :
        print('second Block')
        # did not print because condition is false



# If, Else & Else If Statements
print('\\\\\\\\ If, Else & Else If Statements')

if 1 == 1:

    if 2 > 4:
        print('Hello (if)')
    elif 4 == "4":
        print('Hola (elif)')
    else:
        print('bye (else)')


# For Loop
print('\\\\\ For Loop')

print('\\\\\ For Loop in sequence')
seq = [1,2,3,4,5,6]

for item in seq: # Printing list through for loop
    # Code here
    print(item)
    print('hello')


print('\\\\\ For Loop in  dictionaries')
d = { 'bean':1, 'Naruto':2, 'Thomas':3 }

for k in  d:  # Printing dictionaries through for loop
    print(k)
    print(d[k])


print('\\\\\ For Loop in Tuples')
my_pairs = [(1,2),
            (3,4),
            (5,6)]

for tup1,tup2 in my_pairs:
    print(tup1) #tup1 means col1 in tuple row
    print(tup2) #tup2 means col2 in tuple row


# While Loop
print('\\\\\\ While Loop')
i = 1

while i<5 :
    print(f'i is {i}')
    i = i + 1


# range function
print('\\\\\ range function')
# range function is a generator of values
print(list(range(0,21))) # range function can make lists. (0,21) 0 mean initial index 21 means ending.
print(list(range(0,21,2))) # 2 in last represent step size

# For loop in range
print('\\\\\ For loop in range')

for item in range(6): #printing values from range
    print(item)
    # print('party')

# List Comprehension
print('List Comprehension')

i = [1, 2, 3, 4]
out = []

for num in i: # we want the list numbers to become their square
    out.append(num**2)
print(out)

# another method
print('\\\\\ another method')
i = [1, 2, 3, 4]

out = [num**2 for num in i] # this method consume less space

print(out)