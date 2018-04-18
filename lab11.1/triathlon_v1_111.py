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

	def name(d):
		return d.name


	def __str__(self):
		for t in sorted(self.d, key=name):
			print(t)



