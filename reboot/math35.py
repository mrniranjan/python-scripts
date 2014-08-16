#from sys module import argv feature
from sys import argv
# pass the arguments passed to the respective variables
script, file1, file2 = argv

# open the file that's mentioned in variable file1
target1 = open(file1)

# read the contents of the file and save the contents 
# in variable s1
s1 = target1.read()
# close the file
target1.close()

# open file mentioned in file2 in write mode
target2 = open(file2,'w')
# write the contents of variable s1 in the file 
target2.write(s1)
# close the file 
target2.close()



