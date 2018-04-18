class Triathlete(object):




	def __init__(self, name, tid):
		self.name = name
		self.tid = tid
		self.times = {}

	def __str__(self):
		a = []
		a.append("Name: {}".format(self.name))
		a.append("ID: {}".format(self.tid))
		total = sum(self.times.values())
		a.append("Race time: {}".format(sum(self.times.values())))
		return "\n".join(a)

	def add_time(self, event, time):
		self.times[event] = time

	def get_time(self, event):
		return self.times[event]





def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)
    # print t1.times
    # print sum(t1.times.values())

if __name__ == '__main__':
    main()
