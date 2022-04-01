import pandas

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter: row.code for (index, row) in data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Condition to run program
keep_asking = True

while keep_asking:
# Input a word
    user_string = input("Input your phrase: ").upper()

# Get string and split it into a list with letters
    list_string = [letter for letter in user_string]

    
# Check the letters and return a list with the correspoding nato value

    try:
        nato_string = [nato[letter] for letter in list_string if letter !=' ']

    except KeyError:
        print("Sorry, only letters in the alphabet please")

    else:
        print(nato_string)
        keep_asking = False
