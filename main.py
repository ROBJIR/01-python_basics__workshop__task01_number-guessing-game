from random import randint
# constants:
RANDOM_NUMBER_LOWER_LIMIT = 1
RANDOM_NUMBER_UPPER_LIMIT = 100

def enter_value():
    while True:
        try:
            your_value = int(input(f"Guess the number:"))
            print(f" - your number: {your_value}")
            break
        except ValueError:
            print("It's not a number!")
    return your_value

def guess_number (random_number: int):
    while True:
        your_number = enter_value()
        if your_number>random_number:
            print("Too big!")
        elif your_number<random_number:
            print("Too small!")
        else:
            print("You win!")
            break
    return

# main
print(60*"-"+"\n"+"Python basic / Workshop / task: 01 - Number guessing game"+"\n"+60*"-")

random_number = randint(RANDOM_NUMBER_LOWER_LIMIT, RANDOM_NUMBER_UPPER_LIMIT)
# print(f" - random number: {random_number}")

guess_number(random_number)

print("--- end "+52*"-")