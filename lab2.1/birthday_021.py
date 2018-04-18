import sys
import calendar
days = {
	0 : "Monday",
	1 : "Tuesday",
	2 : "Wednesday",
	3 : "Thursday",
	4 : "Friday",
	5 : "Saturday",
	6 : "Sunday",
}

endings = {
	0 : "is fair of face",
	1 : "is full of grace",
	2 : "is full of woe",
	3 : "has far to go",
	4 : "is loving and giving",
	5 : "works hard for a living",
	6 : "is fair and wise and good in every way",
}


day = int(sys.argv[1])
month = int(sys.argv[2])
year = int(sys.argv[3])

wday = calendar.weekday(year, month, day)

s = days[wday]
end = endings[wday]

print("You were born on a {} and {}'s child {}.".format(s, s, end))