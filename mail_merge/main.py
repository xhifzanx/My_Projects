# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp





with open("./Input/Names/invited_names.txt") as data_2:
    content_2 = data_2.readlines()

with open("./Input/Letters/starting_letters.txt") as data_1:
    content_1 = data_1.read()
    for name in content_2:
        name = name.strip()
        letter = content_1.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode='w') as letters:
            letters.write(letter)





