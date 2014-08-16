def great():
	number = [1, 1, 10, 8, 15, 8, 85]
	count = 0	
	length = len(number) 
	currentlarge = number[count]
	#latest = currentlarge
	for i in number:
		count += 1
		if count <= length-1: 
			if currentlarge > number[count]:
				 latest = currentlarge
			else:
				currentlarge = number[count]
				latest = currentlarge

	print latest

great()
