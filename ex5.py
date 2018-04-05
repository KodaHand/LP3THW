name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # Inches
height_cm = height * 2.54 # centimeters
weight = 180 # Pounds
weight_kilo = weight * 0.45359237 # kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall and {height_cm} centimeters tall.")
print(f"He's {weight} pounds heavy and {weight_kilo} in kilograms.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# spacing
print()

# MY MEASUREMENTS
my_name = 'Tyler G. Hand'
my_age = 21
my_height = 69 # Inches
my_height_cm = my_height * 2.54
my_weight = 260 # Pounds
my_weight_kilo = my_weight * 0.45359237 # kilograms
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
# height rounded with round()
print(f"I'm {my_height} inches tall and {round(my_height_cm)} centimeters tall")
# weight is rounded using round()
print(f"I'm {my_weight} pounds heavy and {round(my_weight_kilo)} in kilograms.")
print("Actually that's not too heavy.")
print(f"I've got {my_eyes} eyes and {my_hair} hair.")
print(f"My teeth are usually {my_teeth} depending on the coffee.")
