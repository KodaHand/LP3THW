print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs.")

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from institution
and requires an explanation
\n\twhere there is none.
"""

print("______________")
print(poem)
print("______________")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secrete_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secrete_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f" " string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secrete_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates".format(*formula))
