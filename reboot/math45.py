#from sys import argv
#script, in_file = argv

def area_of_circle(radius):
	"""This function calculates Area of a circle
	given by formula area = pi * r * r , where pi has a
	value of 3.14 """
	pi = 3.14
	area = pi * radius * radius
	return area 

def circumference_of_circle(radius):
	"""This function calculates circumference of circle
	given by formula circumference = 2 * pi * r where pi has
	value of 3.14 """
	pi = 3.14
	circumference = 2 * pi * radius
	return circumference

def area_of_square(length):
	"""This function calculates area of square
	given by formula: area = length * length """
	area = length * length
	return area


def area_of_rectangle(length, breadth):
	"""This function calculates area of rectangle
	given by formula: area = length * breadth """
	area = length * breadth
	return area

def circle():
        print """
        Radius of a circle is pi * r * r , where r is
        is radius, and pi value is 3.14
        """

        radius = raw_input("Enter radius of circle:");

        area = area_of_circle(int(radius))
        print "Area of circle with radius %r is: %d" % (radius, area)

def circumference():
	print """
	Circumference of a circle is 2 * pi * r, where r is
	radius  and value of pi is 3.14
	"""
	radius = raw_input("Enter radius of circle:");
	
	circumference = circumference_of_circle(int(radius))
	print "Circumpherence of Circle with radius %r is : %d" % (radius, circumference)

def square():
	print """ 
	Area of square is square of length of it's side
	"""
	length = raw_input("Enter length of square: ")
	area = area_of_square(int(length))
	print "Area of square with length %r is: %d" % (length, area)

def rectangle():
	print """
	Area of rectangle is it's length * breadth
	"""
	length = raw_input("Enter length of rectangle: ")
	breadth = raw_input("Enter breadth of rectangle: ")
	area = area_of_rectangle(int(length), int(breadth))
	print "Area of rectange whose length is %r and breadth %r is: %d" % (length, breadth, area)

s1 = """
We will be doing some geomentrical calculations:
\t 1. Area of Circle 
\t 2. Circumference of circle
\t 3. Area of Square
\t 4. Area of rectangle
"""

print s1 
print "Press Enter to Continue or CTRL-C to exit"
raw_input("> ")

print "Enter the Geomentrical calculation you want to learn:" 
myinput = raw_input("> ")

if int(myinput) == 1:
	circle()

if int(myinput) == 2:
	circumference()

if int(myinput) == 3:
	square()

if int(myinput) == 4:
	rectangle()

