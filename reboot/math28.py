price_of_apple_per_kg = 40
price_of_oranges_per_kg = 30
price_of_one_comb = 3
price_of_one_tb = 10
price_of_one_pencil = 1
price_of_one_notebook = 6
price_of_one_soapcake = 8

fruit1 = "Apple"
fruit2 = "Orange"
thing1 = "Combs"
thing2 = "Tooth Brush"
thing3 = "Pencils"
thing4 = "Note Books"
thing5 = "Soap Cakes"

print "\t\tRamans's Shop"
print "\t\t............."
s1 = """
\tThings\t\tPrice
\t%s\t\tRs %d per kg
\t%s\t\tRs %d per kg
\t%s\t\tRs %d for one
\t%s\t Rs %d for one
\t%s\t\tRs %d for one
\t%s\tRs %d for one
\t%s\tRs %d for one
""" % (fruit1, price_of_apple_per_kg, fruit2, price_of_oranges_per_kg,
thing1, price_of_one_comb, thing2, price_of_one_tb, thing3, price_of_one_pencil,
thing4, price_of_one_notebook, thing5, price_of_one_soapcake)

print s1

total_apple_sales = 2457
total_orange_sales = 3004
total_combs_sales = 22760
total_toothbrush_sales = 25367
total_pencils_sales = 38530
total_notebooks_sales = 40002
total_soapcakes_sales = 20005

print "\t\tSales during last year"
print "\t\t......................"
s2 = """
\t%s\t\t\t%d Kg
\t%s\t\t\t%d Kg
\t%s\t\t\t%d
\t%s\t\t%d
\t%s\t\t\t%d
\t%s\t\t%d
\t%s\t\t%d
""" % (fruit1, total_apple_sales, fruit2, total_orange_sales, thing1, total_combs_sales,
thing2, total_toothbrush_sales, thing3, total_pencils_sales, thing4, total_notebooks_sales,
thing5, total_soapcakes_sales)

print s2

s3 = "Weight of Apples = %d kg" % total_apple_sales
s4 = "Weight of Oranges = %d kg" % total_orange_sales

s5 = "Therefore, total weight = %d Kg + %d Kg = %d Kg" % (total_apple_sales, total_orange_sales,
total_apple_sales + total_orange_sales)

total_money_from_apple_sales = total_apple_sales * price_of_apple_per_kg
total_money_from_orange_sales =  total_orange_sales * price_of_oranges_per_kg
total_fruit_sales = total_money_from_apple_sales + total_money_from_orange_sales

s6 = "Total money Raman got by selling %s is: %d" % (fruit1, total_money_from_apple_sales)
s7 = "Total Money got by selling %s and %s is %d" % (fruit1, fruit2 , total_fruit_sales)

print "\t" + s3 + "\n"
print "\t" + s4 + "\n"
print "\t" + s5 + "\n"
print "\t" + s6 + "\n"
print "\t" + s7 + "\n"
