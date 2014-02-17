#!/usr/bin/python
#from sys import argv
#from os.path import exists

def report():
	current_file=open("expenditure.txt", 'r')
	print current_file.read()
	

def getexp():
	x = "Expenditure Sheet"
	y = "*" * 20
	item1 = str(raw_input("Item 1:"))
	item1price = float(raw_input("Enter price for item1:"))
	item2 = str(raw_input("Item 2:"))
	item2price = float(raw_input("Enter price for item2:"))
	item3 = str(raw_input("Item 3:"))
	item3price = float(raw_input("Enter price for item3:")) 
	file = open("expenditure.txt", 'w')
	file.write(x)
	file.write("\n")
	file.write(y)
	file.write("\n")
	file.write(item1)
	file.write(":")
	file.write(str(item1price))
	file.write("\n")
	file.write(item2)
	file.write(":")
	file.write(str(item2price))
	file.write("\n")
	file.write(item3)
	file.write(":")
	file.write(str(item3price))
	file.write("\n")
	file.close()

getexp()
report()


