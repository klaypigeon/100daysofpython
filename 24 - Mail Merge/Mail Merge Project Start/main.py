#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()  # List of Strings

with open("Input/Letters/starting_letter.txt") as f:
    letter = f.read()  # One long string

for name in names:
    new_name = name.strip()
    new_contents = letter.replace("[name]", new_name)
    with open(f"Output/ReadyToSend/Letter_for_{new_name}.txt", "w") as f:
        f.write(new_contents)
