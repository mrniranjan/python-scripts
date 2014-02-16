#!/usr/bin/python

print "Following are the items sold in Rahman's Shop"
print "*" * 50 
apples = 40 
oranges = 30
Combs = 3
Toothbrushes = 10
Pencils = 1
Notebooks = 6
Soapcakes = 8

app = 2457
org = 3004
com = 22760
tb = 25367
pen = 38530
nb = 40002
sc =  20005

x = "Rs %d per kg"
y = "Rs %d for one"

appl = "Apples"
oran = "Oranges"
cmb = "Combs"
tbrush = "Tooth Brushes"
penc = "Pencils"
note = "Note Books"
soap = "Soap Cakes"

print "\t" + appl + "\t\t" + x % apples
print "\t" + oran + "\t\t" + x % oranges
print "\t" + cmb + "\t\t" + y % Combs
print "\t" + tbrush + "\t" + y % Toothbrushes
print "\t" + penc + "\t\t" + y % Pencils
print "\t" + note + "\t" + y % Notebooks
print "\t" + soap + "\t" + y % Soapcakes
print "*" * 50
print 
print "\t" + "Sales during Last year" 
print "*" * 50
print "\t" + appl + "\t\t" + "%d kg" % app
print "\t" + oran + "\t\t" + "%d kg" % org
print "\t" + cmb + "\t\t" + "%d" % com
print "\t" + tbrush + "\t" + "%d" % tb
print "\t" + penc + "\t\t" + "%d" % pen
print "\t" + note + "\t" + "%d" % nb
print "\t" + soap + "\t" + "%d" % sc
print "*" * 50

print "Total Weight of %s sold %d kg" % (appl, app)
print "Total Weight of %s sold %d kg" % (oran, org)
print "Total Weight of %d kg + %d kg is %d kg" % (app,org,app+org)
print "Total Money gained by Raman by selling",
print "Apples is %0.2f" % (app * apples)
print "Total Money gained by Ram by selling",
print "Apples and Oranges to gether is %0.2f" % (app * apples + org * oranges)
