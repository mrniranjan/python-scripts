# declared variable cars with value 100
cars = 100
# declare space_in_a_car variable with value 4.0
space_in_a_car = 4.0
#declare variable drivers with value 30
drivers = 30 
#declare variable passengers with value 90
passengers = 90
#declare cars_not_driven variable which has value determined
#by operation cars - drivers
cars_not_driven = cars - drivers
#declare variable cars_driven, whose value is equivalent
#to value stored in variable drivers
cars_driven = drivers
#declare variable carpool_capacity with value cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#declare variable average_passengers_per_car whose
#value would be based on the output of passengers / cars_driven
average_passengers_per_car = passengers / cars_driven


# print string "There are" and value stored in variable cars and again
# string "cars available"
print "There are", cars, "cars available."
#print string "There are only" , then value stored in variable drivers 
# and string "drivers available"
print "There are only", drivers, "drivers available."
#print string "there will be" then print value stored in 'cars_not_driven' and
#print string "empty cars today"
print "There will be", cars_not_driven, "emty cars today."
#print string "there will be" and value stored in variable 'cars_not_driven' and
#print string "people today"
print "We can transport", carpool_capacity, "people today."
#print string "We had" and value stored in variable 'passengers' 
#and also print string "to carpool today"
print "We have", passengers, "to carpool today."
#print string "We need to put about" and value stored in 'average_passengers_per_car' and 
#string "in each car"
print "We need to put about", average_passengers_per_car, "in each car."
