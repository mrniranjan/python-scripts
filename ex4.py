#!/usr/bin/python

# Declare variable "cars" having value 100
cars = 100 

# Declare variable "space_in_a_car" having value 4.0 (floating point)
space_in_a_car = 4.0

# Declare variable "drivers" having value 30
drivers = 30 

# Declare variable "passengers" having value 90
passengers = 90

# Declare variable "cars_not_driven" having value equivalent "value stored in cars" - "value stored in variable drivers"
cars_not_driven = cars - drivers

# Declare variable 
cars_driven = drivers

# Declare variable "carpool_capacity" which has value determined by expression "cars_driven" * "value stored in variable space_in_a_car"
carpool_capacity = cars_driven * space_in_a_car

# Declare variable "average_passengers_per_car" which has value determined by "value in variable passengers" / "value in variable cars_driven"
average_passengers_per_car = passengers / cars_driven 

# print string "There are" and then we are print value in variable cars, and then print string "cars available"
print "There are", cars, "cars available"

# print string "There are only" "value in varable drivers" and string "drivers available"
print "There are only", drivers, "drivers available" 

# print string "There will be" "value in variable cars_not_driven" , and string "empty cars today"
print "There will be", cars_not_driven, "empty cars today"

# print string "We can transport", value in variable carpool_capacity, and string "people today"
print "We can transport", carpool_capacity, "people today"

# print string "We have" , value stored in variable passengers and string "to carpool today"
print "We have", passengers, "to carpool today"

# print string "We need to put about" , value in variable "average_passengers_per_car"  and string "in each car"
print "We need to put about", average_passengers_per_car, "in each car"



