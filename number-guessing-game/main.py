from random import randint

def is_valid_range():
    while True:
        x, y = input().strip(), input().strip()
        if x.isdecimal() and y.isdecimal():
            return int(x), int(y)
        else:
            print("Invalid range. Please enter two natural numbers: minimum and maximum on separate lines.")

def is_valid(x, y):
    while True:
        n = input("Enter a number: ").strip()
        if n.isdecimal() and x <= int(n) <= y:
            return int(n)
        else:
            print(f"Please enter an integer between {x} and {y}.")

def continue_game():
    while True:
        text = input("Would you like to play again? y = Yes, n = No: ").strip().lower()
        if text in ["n", "no"]:
            print("Thank you for playing the Number Guessing Game. See you next time!")
            return False
        elif text in ["y", "yes"]:
            return True
        else:
            print("I didn't understand your response.")

def game(x, y):
    num = randint(x, y)
    print(f"Guess the number between {x} and {y}.")
    count = 0
    while True:
        n = is_valid(x, y)
        count += 1
        if n == num:
            print("Congratulations! You guessed it!")
            print(f"Number of attempts: {count}")
            return continue_game()
        elif n > num:
            print("Your number is too high. Try again!")
        elif n < num:
            print("Your number is too low. Try again!")

def start_game():
    print("Welcome to the Number Guessing Game!")
    while True:
        print("Choose the range for the random number: enter the minimum and maximum values on separate lines:")
        x, y = is_valid_range()
        if x > y:
            x, y = y, x

        if not game(x, y):
            break


if __name__ == "__main__":
    start_game()
