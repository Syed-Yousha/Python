import random
# \\\\\\\\\\\\\\\\\\ NUMBER GUESSING GAME IN PYTHON \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# \\\\\\\\\\\ User value Functions and error checking
def digits(user):
    u = int(user)

    if u > 999:
        return "error"
    else:
        return int(u)



def no_repeat(user):
    x = str(user)

    if x[0] == x[1] == x[2] or x[0] == x[1] or x[1] == x[2] or x[0] == x[2]:
        return "error"
    else:
        return int(x)


def clues(user, comp):
    u = str(user)
    c = str(comp)

    if u[0] == c[0] and u[1] == c[1] and u[2] == c[2]:
        return " Congrats you successfully guessed the code.."
    elif u[0] == c[0]:
        return "matched"
    elif u[1] == c[1]:
        return "matched"
    elif u[2] == c[2]:
        return "matched"
    elif u[0] in c or u[1] in c or u[2] in c:
        return 'close'
    else:
        return "Try again"

# \\\\\\\\\\\\\\\\\\\\\\ Computer will guess 3 digit non-repeating number:

# def generate_code():
#
#     digit = [str(num) for num in range(10)]
#
#     # shuffle the digit
#     random.shuffle(digit)
#     return digit[:3]
#
#
# comp = generate_code()

comp = 234

# ////////////////////// User Guesses
a = input("enter a 3 digit number : ")
b = digits(a)
user = no_repeat(b)

while user == "error" or user != comp:
    print("Error! p lease enter non-repeating 3 digits eg:123")
    a = input("enter a 3 digit number : ")
    b = digits(a)
    user = no_repeat(b)
    checking = clues(user, comp)
    print(checking)

