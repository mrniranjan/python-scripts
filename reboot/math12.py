student1 = "Ramahari"
student2 = "Dolly"
student3 = "Mohan"
student4 = "Shashi"

s1cm = 160
s2cm = 154
s3cm = 158 
s4cm = 159

s1 = "let's check who is tallest of %s(%d)cm , %s(%d)cm, %s(%d)cm, %s(%d)" % (student1, s1cm, student2, s2cm, student3, s3cm, student4, s4cm)

s2 = "Is %s taller than %s :" % (student1, student2)
s3 = "Is %s taller than %s :" % (student2, student3) 
s4 = "Is %s taller than %s :" % (student3, student4)

print s1
print s2 , s1cm > s2cm 
print s3 , s2cm > s3cm 
print s4 , s3cm > s4cm





