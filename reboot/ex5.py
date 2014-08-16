# declare variable name containing string 'Zed A. Shaw'
name = 'Zed A. Shaw'
# declare variable age containing numeric value 35
age = 35
# declare variable height containing numeric value 74
height = 74
# declare variable weight containing numeric value 180
weight = 180
#declare variable eyes containing string 'Blue'
eyes = 'Blue'
#declare variable teeth containing string 'White'
teeth = 'White'
#declare variable hair containing string 'Brown'
hair = 'Brown'

#print string "Let's talk about %s", where %s is format string
#which evaluates to variable name which contains string value
print "Let's talk about %s." % name
#print string "He's %d inches tall", %d is format
#string which evaluates to variable height which contains 
#numeric value 74
print "He's %d inches tall." % height
#print string "He %d inches tall", where %d
#evaluates to value stored in variable weight
print "He's %d pounds heavy." % weight
#print string "Actuall that's not too heavy"
print "Actually that's not too heavy."
#print string "He's got %s eyes and %s hair", %s 
# would evaluate to value stored in eyes and hair respectively
print "He's got %s eyes and %s hair." % (eyes, hair)
#print string "His teeth are usually %s depending on the coffee
# where %s evaluates to value stored in teeth variable
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
#print string "If i add %d %d and %d I get %d", 
# first %d evaluates to the value stored in age
# 2nd %d evaluates to value stored in weight
# 3rd %d evaluates to value stored in age
# 4th %d evaluates to addition of values stored in age + height + weigh
print "if i add %d %d , and %d I get %d." % (
      age, height, weight, age + height + weight)
