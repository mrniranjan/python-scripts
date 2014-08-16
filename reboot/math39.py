def func():
	print "Write the next 3 natural numbers after 10999"
	number1 = raw_input("Enter number1: ")
	n1 = 10999 + 1
	check1 = int(number1) == n1
	number2 = raw_input("Enter number2: ")
	n2 = n1 + 1
	check2 = int(number2) == n2
	number3 = raw_input("Enter number3: ")
	n3 = n2 + 1
	check3 = int(number3) == n3

	print "The next 3 natural numbers after 10999 are %d,%d,%d" % (n1,n2,n3)
	print "let's see if the numbers which you have entered were correct"
	print "Is number1 equal to desired result %d: %s" % (n1, check1)
	print "Is number2 equal to desired result %d: %s" % (n2, check2)
	print "Is number3 equal to desired result %d: %s" % (n3, check3)


func()
