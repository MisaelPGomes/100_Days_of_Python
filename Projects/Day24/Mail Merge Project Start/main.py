


# First step is to save the names from the invited_names.txt file to a list of names:

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    print(names)

# Since the generated list comes with \n. This part of the code generates a new list of names without \n.
# It is obtained using the strip method to remove parts of the text we do not want.
# The replace method enables the code to change a piece of the string and replace it with something else.

new_names = []
for name in names:
    new_name = name.strip("\n")
    with open("./Input/Letters/starting_letter.txt") as f:
        text = f.read()
        x = text.replace("[name]", new_name)

        with open(f"Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as letter_file:
            letter_file.write(x)

            # Using os library it was possible to rename the file with each person of the list



