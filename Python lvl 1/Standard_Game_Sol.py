import random

# GET GUESS

def get_guess():
    return list(input("What is your guess?  :"))

# Generate Computer code 123

def generate_code():
    digits = [str(num) for num in range(10)]

    # Shuffle the digit
    random.shuffle(digits)
    return digits[:3]

# Generate The Clues

def generate_clues(code, user_guess):


    if user_guess == code:
        return "Code Cracked"

    clues = []

    ind = 0
    for ind, num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")

        if clues == []:
            return ["nope"]
        else:
            return clues


# Run game logic

print("Welcome code breaker!")

secret_code = generate_code()

clue_report =[]

while clue_report != "code craked!":

    guess = get_guess()

    clue_report = generate_clues(guess, secret_code)
    print("here is the result of your guess:  ")
    for clue in clue_report:
        print(clue)