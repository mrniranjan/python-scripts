def Prime_List(num):
	""" This function returns list of prime Numbers
	from 0 to N, where N is number given as argument
	"""
	Prime_List = []
	for i in range(2, num+1):
		if i == 2:
			Prime_List.append(i)
		else:
			count = 2
			y = i // 2
			temp = 0
			if count > y:
				Prime_List.append(i)
			else:
				while count <= y:
					temp = i % count
					if temp == 0:
						break
					else:
						count += 1
				if temp != 0:
				  Prime_List.append(i)
	return Prime_List


def main():
	""" Main function calling Prime_List """
Number = raw_input("Enter any Number between 1 to 100:  ")
Number = int(Number)
dict = {}

for i in range(0, Number):
	result = Prime_List(i)
	for j in range(0, len(result)):
		dict.setdefault(i, []).append(result[j])

for key,value in dict.items():
	print "For Number %d, the range of Prime Numbers from 1 to %d are: %s" % (key, key, dict[key])
	
	

if __name__ == '__main__':
	main()

