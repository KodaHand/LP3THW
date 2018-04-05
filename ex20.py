# imports argv from sys
from sys import argv

# defines args for argv. Always have to start with script for some reason
script, input_file = argv

# function that prints all of a file
def print_all(f):
    print(f.read())

# function that rewinds to the beginning of the file. Without this it will continue where the print_all function left off
def rewind(f):
    # seek(0) tells it to go back to the beginning
    f.seek(0)

# function that prints a line and takes two arguments, what line its on and what file its reading
def print_a_line(line_count, f):
    ###  You can add , end = "" at the end to not get spaces between them. ###
    print(line_count, f.readline(), end = "") # get rid of that to figure out what im talking about. You will put it back, it makes it look nicer

# opens a file of your choice that was passed in via argv
current_file = open(input_file)

# printing
print("First let's print the whole file:\n")

# Calls function and passes in the current file
print_all(current_file)

# printing
print("Now let's rewind, kind of like a tape.")

# calls rewind function and rewinds back through the file to the beginning useing the seek(0)
rewind(current_file)

# printing
print("Let's print three lines:")

# makes current line = 1 so that it starts at the beginning
current_line = 1
#prints the line based on whatever line current_line is on
print_a_line(current_line, current_file)

# continues what I described above
current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
