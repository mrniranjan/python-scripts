s1 = "." * 40		# declare variable s1 which contains a string "........" (dots) ,40 dots
mtr = "Metre"		# declare variable mtr storing string "Meter"
cm = "Centimeter"
mm = "Millimeter"
km = "Kilometer"

print "Let's do some more examples" 
print s1
s2 = "let's write conversion tables"

s3 = "1 %s is 1000 %s" % (mtr, mm)
s4 = "1 %s is 100 %s" % (mtr, cm)
s5 = "1 %s is 1000 %s" % (km, mtr)

print s2 
print s3 
print s4 
print s5
print s1
mycm = 20120
mymtr = 1501
mymm = 340101
mykm = 15

cmtomm = mycm/100
mtrtocm = mymtr * 100 
mmtomtr = mymm / 1000
mtrtokm = mymtr / 1000
kmtomtr = mykm * 1000
mykmtomm = mykm * 1000 * 1000 


mys = "%d %s is equal to %d %s" 

print mys % (mycm, cm, cmtomm, mm)
print mys % (mymtr, cm, mtrtocm, cm)
print mys % (mymm , mm, mmtomtr, mtr)
print mys % (mykm , km, kmtomtr, mtr)
print mys % (mykm, km, mykmtomm, mm)
print s1
