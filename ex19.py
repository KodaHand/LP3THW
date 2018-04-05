# defines a function and has two arguments, cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # next four and just prints with some formats
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# more printing
print("We can just give the function numbers directly:")
# calls the function cheese_and_crackers and gives cheese_count 20 and boxes_of_crackers 30
cheese_and_crackers(20, 30)

#more prints
print("OR, we can use variables from our script:")
# defines the amount of cheese
amount_of_cheese = 10
# defines the amount of crackers
amount_of_crackers = 50

# calls cheese_and_crackers and inserts amount_of_cheese and amount_of_crackers which are ints in for cheese_count and boxes_of_crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints more stuff
print("We can even do math inside too:")
# calls cheese_and_crackers and puts in amounts with math
cheese_and_crackers(10 + 20, 5 + 6)

# printing never gets old
print("And we can combine the two, variables and math:")
# calls cheese_and_crackers and puts vars used above in and does math for the rest
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
