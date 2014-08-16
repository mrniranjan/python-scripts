from sys import exit, argv
import random

script, player_name = argv


def start_game(player_name):
	s1 = ("Greetings %s, Welcome to \n"
	      "Business game. The idea of this game\n"
	      "is to know how you would utilize the money.\n"
	      "The Goal is to make good use of money and also \n"
	      "enjoy life and yet make enough profits.\n"
	      "So ready to roll ?(yes/no)\n"
	     ) % player_name

	s2 = """
	Okay %s, Good bye
	""" % player_name

	print s1
	ok_start = raw_input("Press Enter to continue or CTRL-C to break")
	
	if ok_start == '':
		print "We are inside the if statement"
		rules(player_name)
	else:	
		print s2
		exit(0)

def rules(player_name):

	print """
	Okay %s, Here are rules:
	-> You will be given 50000$, which you would have to invest 
	-> Based on your Investment pattern, You will be awarded points
	-> You will be rolling a die, depending on the number you get , you
	will be shown different options to invest/spend, have to choose the option
	""" % player_name

        print """
        %s, Die has 3 Numbers, When rolled,
        Depending upon the Number returned,
        Following options will be choosen:

        1. Buy a house
        2. Buy Jwellery
        3. Go to Party
        """ % player_name

	print "Ready to roll the die:?"
	roll = raw_input("y/n: ")

	if roll == 'y':
		play_init(player_name)
	else:
		exit(0)

def play_init(player_name):

        base_amount = 50000
        game_points = 0
	play_game(player_name,base_amount,game_points)

def roll_die():
	die = random.randint(1, 2)
	return die

def play_game(*args):

	player_name, base_amount, game_points = args

	die_number = roll_die()
	print "Die rolled and you got Number %d" % die_number

	if die_number == 1:
		point_earned = buy_a_house(player_name,base_amount,game_points)

	elif die_number == 2:
		point_earned = buy_a_jwellery(player_name,base_amount,game_points)

	elif die_number == 3:
		point_earned = go_to_la(player_name,base_amount,game_points)

def buy_a_house(player_name,base_amount,game_points):

	three_bhk_price = 15000
	two_bhk_price = 12000
	villa_price = 0
	three_bhk_rent = 800
	three_bhk_points = 20
	two_bhk_points = 5
	villa_point = 0

	if base_amount > two_bhk_price:

		print """ 
			%s, You have 3 Options: pick one
			1. 3 Bedroom Apartment Costing 1500$ [Rent-800$]
			2. 2 Bedroom Apartment Costing 1200$ [Rent-900$]
			3. Villa Costing
		""" % player_name
		next = raw_input("> ")
		if next == '1':
			base_amount = base_amount - three_bhk_price
			game_points = game_points + three_bhk_points
		
			print "Do you want to give it on rent(yes/no): "
			rent_opt = raw_input("> ")
		
			if rent_opt == 'yes':
				bonus = game_points * 2
		if next == '2':

			base_amount = base_amount - two_bhk_price		
			game_points = game_points + two_bhk_points

			print "Do you want to give it on rent(yes/no):"
			rent_opt = raw_input("> ")
		
			if rent_opt == 'yes':
				bonus = game_points * 2

		if next == '3':
			print """
			%s, You do not have sufficient funds, 
			To buy a villa, but to buy you will have to
			go to LA and get some money.
			""" % player_name
			next = raw_input("What do you say: ")
			if next == 'yes':
				go_to_la(player_name,base_amount,game_points)
			else:
				print "please pay the game again"
				play_game(player_name,base_mount,game_points)
	
	else:
		print "You do not have enough money, Do you want to start Again:"
                again = raw_input("y/n: ")
                if again == 'y' or again == '':
                	rules(player_name)
		else:
                	print "Thanks for playing %s" % player_name
	                exit(0)

	print "Amount Remaining: %d" % base_amount
	print "Points Earned: %d" % game_points
	play_game(player_name,base_amount,game_points)
	
def buy_a_jwellery(player_name,base_amount,game_points):
	
	diamond_jwellery = 15000
	gold_jwellery = 8000
	platinum_jwellery = 9000
	diamond_points = 2
	gold_points = 5
	platinum_points = 5

	if base_amount > gold_jwellery:

		print """
		%s you have 3 options, 
		1. Diamond Jwellery
		2. Gold Jwellery
		3. Platinum Jwellery
		""" % player_name

		next = raw_input("Enter your option:")
	
		if next == "1":
			base_amount = base_amount - diamond_jwellery
			game_points = game_points + diamond_points

		elif next == "2":
			base_amount = base_amount - gold_jwellery
			game_points = game_points + gold_points
	
		elif next == "3":
			base_amount = base_amount - platinum_jwellery
			game_points = game_points + platinum_points

		else:
			print "please pay the game again"
			play_game(player_name,base_mount,game_points)

	else:
        	print "You do not have enough money, Do you want to start Again:"
	        again = raw_input("y/n: ")
                if again == 'y' or again == '':
                        rules(player_name)
                else:
                        print "Thanks for playing %s" % player_name
                        exit(0)

        print "Amount Remaining: %d" % base_amount
        print "Points Earned: %d" % game_points
	play_game(player_name,base_amount,game_points)

start_game(player_name)
