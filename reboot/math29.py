from sys import argv

script, number = argv

prompt = ': '

print "Enter another number"
divisor = raw_input(prompt)
print "%s program checks if the %r is divisible by %r or not"  % (script, number, divisor)

output = int(number) % int(divisor)

print "and answer is: %r" % (output == 0) 


