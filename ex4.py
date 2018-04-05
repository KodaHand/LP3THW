#How many cars there are
cars = 100
#How much space is in a car
space_in_a_car = 4.0
#How many drivers there are
drivers = 30
#How many passengers there are
passengers = 90
#Figuring out how many cars are not driven by taking cars (100) minus drivers (30)
cars_not_driven = cars - drivers
#Figuring out how many cars are driven. This is equal to the number of drivers
cars_driven = drivers
#This is how many people we can take as carpoolers. drivers (30) multiplied by space in car (4.0)
carpool_capacity = cars_driven * space_in_a_car
#Figuring out how many passengers can be in one car. Passengers (90) divided by cars driven (30)
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
