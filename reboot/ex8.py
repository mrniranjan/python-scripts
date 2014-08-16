# declare variable formatter which stores any 4 values
# these values will be replaced by the actual values 
# that will be given in further statements
formatter = "%r %r %r %r"

# prints the values stored in formatter , in this case %r would be replaced
# by value 1, and so on 
print formatter % (1, 2, 3, 4)
# print 4 strings 
print formatter % ("one", "two", "three", "four")
# print 4 boolean values
print formatter % (True, False, False, True)
#print variable 4 times, which is "%r %r %r %r"
print formatter % (formatter, formatter, formatter, formatter)
#print the below 4 strings
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So i said god night."
)
