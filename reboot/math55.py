def calculate_shift():
	days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	day_count = 0
	index_count = 0
	hours = {}

	for i in days_of_week:
		#print "When i is: %r" % i 
		if day_count == index_count:
			the_day = days_of_week[index_count]
			#print "value of the_day = %r when i is %r" % (the_day, i)
			hours[the_day] = raw_input("Enter shift hours for" +str(the_day)+" :")
			day_count += 1
			index_count += 1
		#print "At the end of for loop value of day_count: %d" % day_count
		#print "At the end of for loop value of index_count: %d" % index_count
	print hours


calculate_shift()

