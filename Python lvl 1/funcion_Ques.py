# \\\\\\\\\\\\\\\\\ Function Test \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# Question 1
#  Function will return True if [1,2,3] is in the list else False.
print('\\\\\\\ Question 1')

def array_check(nums):

    if 1 in nums and 2 in nums and 3 in nums:
        return True
    else:
        return False

x = array_check([1, 2, 3, 4])
print(x)


# Question 2
# Make a function which will return values like this;

# string_bits('Hello') -> 'Hlo'
# string_bits('Hi') -> 'H'
# string_bits('Heeololeo') -> 'Hello'
print('\\\\\\\ Question 2')

def string_bits(str):

    if type(str) == type('Hello') == type("hi"):
        return str[::2]
    else :
        return "enter string please"


x = string_bits('Heeololeo')
print(x)


# Question 3
print('\\\\\\\ Question 3')

def end_other(a, b):

    a = a.lower()
    b = b.lower()

    if a[-1] == b[-1] and a[-2] == b[-2] and a[-3] == b[-3]:
        return True
    else:
        return False


x = end_other("Hiabc", "abc")
print(x)


x = end_other("AbC", "HiaBc")
print(x)


x = end_other("a"abXabcbc", ")
print(x)


# Question 4
# example double_char('Hello') = 'HHeelloo'
#
# def double_char(val):
#
#     l = len(val)
#     copy = ''
#     x = 0
#     while x <= l:
#         copy = val[x]
#         copy = copy + copy
#         print(copy)
#         x = x + 1
#
#
# double_char('hello')


# Question 5
# no_teen_sum(1,2,3) -> 6
# no_teen_sum(1,2,13) -> 3
# 13 To 10 -> 0, except 15,16
def no_teen_sum(a, b, c):

    if a >= 13 and a <= 19:
        if a != 15 or a != 16:
            a = 0
    if b >= 13 and b <= 19:
        if b != 15 or b != 16:
            b = 0
    if c >= 13 and c <= 19:
        if c != 15 or c != 16:
            c = 0

    return a+ b + c


x = no_teen_sum(1,2,13)
print(x)



# Quesion 6
# count he and print the number of even integer in the list/array

my_list = [1,2,3,4,5,6,7,2,2,2,2]
# length = 0
def count_even(num):
    return num % 2 == 0


x = filter( count_even, my_list)
count = len( list(x) )
print(count)


