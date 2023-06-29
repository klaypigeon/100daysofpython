"""with open("my_file.txt") as file:
    contents = file.read()
    print(contents)"""


with open("my_file2.txt", mode="a") as file:
    contents = file.write("New Text\n")
    print(contents)
