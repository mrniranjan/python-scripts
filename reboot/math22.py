print "We will do some Geomentrical examples"
tri = "Triangle"
rec = "Rectangle"
tra = "Trapezoid"

string1 = "Let's calculate Area of %s" 

line = "." * 40
s1 = """
\t Area of %s 
\t ----------------
\t Area = 1/2 * b * h
\t   b = base
\t   h = vertical height
""" % tri
s2 = """
\t Area of %s
\t ------------------
\t Area = W * h
\t   w = width
\t   h = height
""" % rec

s3 = """
\t Area of %s
\t -----------------
\t Area = 1/2(a+b) * h
\t  h = Vertical height
""" % tra

tri = "Triangle"


print s1
base = raw_input("Enter base:")
height = raw_input("Enter height:")
area_of_triangle =  int(base) * int(height) * 1/2 
print """
Area of %s with %s as base, %s as height is %d
""" % (tri, base, height, area_of_triangle)
print line
print s2
width = raw_input("Enter Width of rectangle: ")
height = raw_input("Enter height of rectangle: ")
area_of_rectangle = int(width) * int(height)
print """
Area of %s with %s as width, and %s  as height is %d 
""" % (rec, width, height, area_of_rectangle)
print line
print s3
width1 = raw_input("Enter the value of a: ")
width2 = raw_input("Enter the value of b: ")
height = raw_input("Enter height: ")
area_of_trapezoid = int(height) * (int(width1) + int(width2)) * 1 / 2
print """
Area of %s when a is %s, b is %s and Height is %s : %d
""" % (tra, width1, width2, height, area_of_trapezoid)
