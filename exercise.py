


def check_letter():
    # Prompt the user to enter a letter (either uppercase or lowercase)
    letter = input("Enter a letter (a-z or A-Z): ").lower()  # Convert to lowercase to simplify checking

    # Check if the input is a single alphabetical character
    if len(letter) == 1 and letter.isalpha():
        # Check if the letter is a vowel
        if letter in "aeiou":
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single alphabetical character.")

# Call the function to run the code
check_letter()


