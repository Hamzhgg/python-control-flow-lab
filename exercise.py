# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

print('-----------------------------------------------------------')


def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()

    if len(letter) == 1 and letter.isalpha():
        if letter in "aeiou":
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical character.")

check_letter()


('-----------------------------------------------------------')


def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative!")
        else:
            if age >= 18:
                print("You are eligible to vote.")
            else:
                print("You are not eligible to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function
check_voting_eligibility()

('-----------------------------------------------------------')


