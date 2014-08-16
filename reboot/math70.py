# using list creat a mapping of a number and it's factors
#example:
#factors = {
#	 4: 1, 2
#	 6: 1, 2, 3
#	 8: 1, 2, 4, 
#}
#import collections

def factors():
	num = 8
	dict = {}
	#dict_data = collections.defaultdict(list)
	for i in range(1, num):
		result = []

		count = 1
		while count <= i:
			temp = i % count
			if temp == 0:
				result.append(count)

			count += 1
		dict.setdefault(i,[]).append(result)
		#dict_data[i].append(result)
		#print result
	print dict
	#list1 = []
	#list1 =  dict[2]	
	#print list1

factors()
