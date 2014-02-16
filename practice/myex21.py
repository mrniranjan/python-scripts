#!/usr/bin/python 
## Let's print a reverse of a number

num = raw_input("Enter a 5 digit number:")
num = int(num)

x1 = num % 10 
num = num / 10 
x2 = num % 10 
num = num / 10 
x3 = num % 10
num = num / 10
x4 = num % 10 
num = num / 10
x5 = num % 10 

num = x1 * 10000 + x2 * 1000 + x3 * 100 + x4 * 10 + x5
print num



