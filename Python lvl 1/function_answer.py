# \\\\\\\\\\\\\\\\\ Function Test \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Question 1
#  Function will return True if [1,2,3] is in the list else False.

def array_check(nums):

    for i in range(len(nums)-2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


# Question 2
# Make a function which will return values like this;
# string_bits('Hello') -> 'Hlo'
# string_bits('Hi') -> 'H'
# string_bits('Heeololeo') -> 'Hello'

# Without slicing (standard way)
def string_bits(mystring):

    result = ''

    for i in range( len(mystring)):

        if i%2 == 0:
            result = result + mystring[i]

    return result



# With Slicing ( Best way)
def slice_str(mystring):

    return mystring[::2]


# Question 3
def end_other(a,b):
    a = a.lower()
    b = b.lower()


    # return (b.endswith(a) or a.endswith(b))
    return a[-len(b):] == b or a == b[-len(a):]

x = end_other('abc','Hiabc')
print(x)

# Question 4
# example double_char('Hello') = 'HHeelloo'

def double_char(mystring):

    result = ''
    for char in mystring:

        result += char*2

    return result


x = double_char('hello')
print(x)



# Question 5
# no_teen_sum(1,2,3) -> 6
# no_teen_sum(1,2,13) -> 3
# 13 To 19 -> 0, except 15,16
print('/////// Question 5')

def no_teen_sum(a, b, c):

    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):

    if n in [13,14,17,18,19]:
        return 0
    return n

x = no_teen_sum(11, 12, 13)
print(x)


# Quesion 6
# count  and print the number of even integer in the list/array

print('\\\\\\ Question 6')
def even(nums):
    count = 0

    for elements in nums:
        if elements % 2 == 0:
            count += 1

    return count

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 5, 4, 3, 2, 1]
x = even(list)
print(x)


