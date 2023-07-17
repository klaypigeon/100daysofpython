import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
ring = {row.letter: row.code for (index, row) in df.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
go = True
while go:
    user_word = input("Word to decode?").upper()
    if not user_word.isalpha():
        print("Must be only letters")
        continue
    if user_word == "EXIT":
        go = False
    word_decoded = [ring[letter] for letter in user_word]
    print(word_decoded)

