# declares types of people
types_of_people = 10
# x is now equal to a string while putting types_of_people in it
x = f"There are {types_of_people} types of people."

# declares binary
binary = "binary"
# declares do_not
do_not = "don't"
# makes y a string and puts binary and do_not into it
y = f"Those who know {binary} and those who {do_not}"

# prints x
print(x)
# prints y
print(y)

# prints a string and puts in x
print(f"I said: {x}")
# prints a string and puts in y
print(f"I also said: '{y}'")

# declares hilarious as false
hilarious = False
# joke_evaluation declaration as a string and puts in hilarious
joke_evaluation = f"Isn't that joke so funny?! {hilarious}"

# .format takes the format of the string because joke_evaluation is a string
# It reformats hilarious which is a bool into a string to be able to print
print(joke_evaluation.format(hilarious))

# declares w a string
w = "This is the left side of..."
# declares e a string
e = "a string with a right side."

# prints w + e
print(w + e)