states = {
	'Andhra Pradesh' : 'AP',
	'Arunachal Pradesh' : 'AR',
	'Andaman & Nicobar Islands' : 'AN',
	'Assam' : 'AS',
	'Bihar' : 'BR',
	'Chandigarh' : 'CH',
	'Delhi' : 'DL'
}

cities = {
	'AP' : 'Hyderabad',
	'AR' : 'Itanagar',
	'AN' : 'Port Blair',
	'AS' : 'Dispur',
	'BR' : 'Patna',
	'CH' : 'Chandigarh',
	'DL' : 'Delhi'
}

# add some more Cities'
cities['KA'] = 'Banglore'
cities['TN'] = 'Chennai'

# print out some cities
print "-" * 10
print "TN state has:", cities['TN']
print "BR state has:", cities['BR']
print "DL state has:", cities['DL']

# print out some states
print "-" * 10
print "Andhra Pradesh abbreviation is: " , states['Andhra Pradesh']
print "Assam abbreviation is: ", states['Assam']

#do it by using the state then cities dict
print "-" * 10
print "Andaman and Nicobar islands has: ", cities[states['Andaman & Nicobar Islands']]
print "Assam has: ", cities[states['Assam']]

# print every state abbreviation
print "-" * 10
for state, abbrev in states.items():
	print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print "-" * 10
for abbrev, city in cities.items():
	print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s" % (
		state, abbrev, cities[abbrev])

print '-' * 10
# safe get a abbreviation by state that mignt not be there
state = states.get('Manipur', 'MN')

if not state:
	print "Sorry, No Manipur"

# get a city with default value
city = cities.get('TX', 'Does not Exist')
print "The city for the state 'TX' is: %s" % city

	

