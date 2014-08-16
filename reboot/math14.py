# this program illustrate usage of raw_input

print "Let's take some more examples"
sub1 = "Maths"
sub2 = "Science"
sub3 = "Social"
sub4 = "Hindi"

s1 = "Please enter marks for %s subject" 

print s1 % sub1, 
sub1mark = raw_input()

print s1 % sub2,
sub2mark = raw_input()

print s1 % sub3,
sub3mark = raw_input()

print s1 % sub4,
sub4mark = raw_input()

totalmarks = int(sub1mark) + int(sub2mark) + int(sub3mark) + int(sub4mark)

s2 = """
Total Marks for subjects:\n
\t%s : %d \n
\t%s : %d \n
\t%s : %d \n
\t%s : %d \n
\tTotal : %d \n
"""
print s2 % (sub1, int(sub1mark), sub2, int(sub2mark), sub3, 
int(sub3mark), sub4, int(sub4mark), totalmarks)

