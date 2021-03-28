#file = open("my_file.txt")
#contents = file.read()
#print(contents)
#file.close()

#with open("my_file.txt") as file:
#    contents = file.read()
#    print(contents)

# You do not need close if you use with

# r is read, w is write, a is append

#with open("my_file.txt", mode="a") as file:
#    file.write("\nNew Text")


#with open("new_file.txt", mode="w") as file:
#    file.write("If no file exists, in write mode, it creates a new file")

# Root is the Macintosh HD, signal by a single forward slash

# Absolute File Path
#    /Work/Project/talk.ppt

# Relative Path
# Imagine we are already in the Project folder, the "working directory"
#   ./talk.ppt              #The dot means, current folder

#Relative folder, to parent folder is two dots.
#   ../report.doc

with open("/Users/christophermayes/Desktop/my_file.txt", mode="w") as file:
    file.write("hello this is a test")

#Relative is relative to current directory, absolute is compared to your MacintoshHD



