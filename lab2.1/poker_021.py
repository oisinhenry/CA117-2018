import sys

# counters

nothing = 0.0
one_pair = 0.0
two_pair = 0.0
three = 0.0
straight = 0.0
flush = 0.0
full_house = 0.0
poker = 0.0
straight_flush = 0.0
royal_flush = 0.0
x = 0.0
for line in sys.stdin:

	x += 1.0
	line = line.strip()
	if line[-1] == "0":
		nothing += 1.0
	elif line[-1] == "1":
		one_pair += 1.0
	elif line[-1] == "2":
		two_pair += 1.0
	elif line[-1] == "3":
		three += 1.0
	elif line[-1] == "4":
		straight += 1.0
	elif line [-1] == "5":
		flush += 1.0
	elif line[-1] == "6":
		full_house += 1.0
	elif line[-1] == "7":
		poker += 1.0
	elif line[-1] == "8":
		straight_flush += 1.0
	elif line[-1] == "9":
		royal_flush += 1.0


# print(nothing)
# print(x)
print("The probability of nothing is {:.4%}".format(nothing / x)) 
print("The probability of one pair is {:.4%}".format(one_pair / x))
print("The probability of two pairs is {:.4%}".format(two_pair / x))
print("The probability of three of a kind is {:.4%}".format(three / x))
print("The probability of a straight is {:.4%}".format(straight / x))
print("The probability of a flush is {:.4%}".format(flush / x))
print("The probability of a full house is {:.4%}".format(full_house / x))
print("The probability of four of a kind is {:.4%}".format(poker / x))
print("The probability of a straight flush is {:.4%}".format(straight_flush / x))
print("The probability of a royal flush is {:.4%}".format(royal_flush / x))