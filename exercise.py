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


def calculate_dog_years():
    try:
        age = int(input("Input a dog's age: "))
        if age < 0:
            print("Age cannot be negative!")
        elif age <= 2:
            dog_years = age * 10
        else:
            dog_years = 20 + (age - 2) * 7
        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Call the function
calculate_dog_years()


('-----------------------------------------------------------')


def weather_advice():
    cold = input("Is it cold? (yes/no): ").strip().lower()
    raining = input("Is it raining? (yes/no): ").strip().lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with 'yes' or 'no'.")

# Call the function
weather_advice()

('-----------------------------------------------------------')


def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").strip().title()
    try:
        day = int(input("Enter the day of the month: "))
        if month in ["Dec", "Jan", "Feb"]:
            if (month == "Dec" and day >= 21) or (month == "Mar" and day <= 19):
                season = "Winter"
            else:
                season = "Winter"
        elif month in ["Mar", "Apr", "May", "Jun"]:
            if (month == "Mar" and day >= 20) or (month == "Jun" and day <= 20):
                season = "Spring"
            else:
                season = "Spring"
        elif month in ["Jun", "Jul", "Aug", "Sep"]:
            if (month == "Jun" and day >= 21) or (month == "Sep" and day <= 21):
                season = "Summer"
            else:
                season = "Summer"
        elif month in ["Sep", "Oct", "Nov", "Dec"]:
            if (month == "Sep" and day >= 22) or (month == "Dec" and day <= 20):
                season = "Fall"
            else:
                season = "Fall"
        else:
            print("Invalid month. Please enter a valid month.")
            return
        print(f"{month} {day} is in {season}.")
    except ValueError:
        print("Invalid day. Please enter a valid number.")

# Call the function
determine_season()

