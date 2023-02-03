# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# using the "with-as" mechanism, we remove the need to open and close a file in the other way
# mode is read/write/append "r" or "w" or "a"

# write
with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

# write
# with open("my_file.txt", mode="w") as file:
#     file.write("New Text.")

# append
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")

# creates a new file if the file does not exist
# with open("new_file.txt", mode="w") as file:
#     file.write("New Text and New File.")

