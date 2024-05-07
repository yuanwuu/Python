# r = Read
# a = Append
# w = Write
# x = Create

import os

# Read - error if it doesn't exit
f = open("names.txt")
# print(f.read())
# print(f.read(4)) #Dave

# print(f.readline())#Dave
# print(f.readline())#Jane

for line in f:
    print(line)

# it's important to close the file when finish, if by any chances, your made changes to the opened file, changes will not reflect until the next time the file opens.
f.close()


try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()

# Append - creates the file if it doesn't exist
f = open("names.txt", "a")
f.write("Neil\n")
f.close()

f = open("names.txt")
print(f.read())  # "Neil" had been added to the file
f.close()

# Write (overwrite)
f = open("context.txt", "w")  # it's in "w" mode
f.write("I deleted all of the context")  # overwrite the file
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# Opens a file for writing, creates the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but returns an error if the file exists
if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x")
    f.close()

# Delete a file

# avoid an error if it doesn't exist
if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")


# with has built-in implicit exception handling
# close() will be automatically called
with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
