def repeat(s, exclaim):
	""" Returns the string s repeated 3 times
	if exclaim is true,  add exclaimation mark.
	"""
	result = s * 3
	if exclaim:
		return result + "!!!"
	else:
		return result

def main():
	print repeat('Yay', False)
	print repeat('WooHoo', True)

	name = "Guido"
	
	if name == 'Guido':
		print repeeet(name) + '!!!'
	else:
		print repeat(name, True)

if __name__ == '__main__':
	main()

