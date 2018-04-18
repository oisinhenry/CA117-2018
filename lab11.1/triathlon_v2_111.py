import operator
class Triathlete(object):

	def __init__(self, name, tid):
		self.name = name
		self.tid = tid

	def __str__(self):
		a = []
		a.append("Name: {}".format(self.name))
		a.append("ID: {}".format(self.tid))
		return "\n".join(a)


class Triathlon(object):


	def __init__(self):
		self.d = {}

	def add(self, athlete):
		self.d[athlete.tid] = athlete

	def remove(self, n):
		if n in self.d:
			del self.d[n]

	def lookup(self, n):
		if n in self.d:
			return self.d[n]
		else:
			return None




	def __str__(self):
		a = []
		for athlete in (sorted(self.d.values(), key=operator.attrgetter("name"))):
			a.append(str(athlete))
		return "\n".join(a)



