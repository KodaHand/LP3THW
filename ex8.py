# declares a variable called formatter and inserts 4 {} as a string
formatter = "{} {} {} {}"

# prints a string and formats into formatter
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, False))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
	"Try your",
	"own text here,",
	"maybe a poem,",
	"or a song about fear"
))
