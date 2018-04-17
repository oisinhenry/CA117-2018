class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.times = {}
        self.total = sum(self.times.values())

    def __str__(self):
        a = []
        a.append("Name: {}".format(self.name))
        a.append("ID: {}".format(self.tid))
        total = sum(self.times.values())
        a.append("Race time: {}".format(sum(self.times.values())))
        return "\n".join(a)

    def add_time(self, event, time):
        self.times[event] = time
        self.total = sum(self.times.values())

    def get_time(self, event):
        return self.times[event]

    def __gt__(self, other):
        return self.total > other.total

    def __lt__(self, other):
        return self.total < other.total

    def __eq__(self, other):
        return self.total == other.total

import operator
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
        for athlete in (sorted(self.d.values(), key = operator.attrgetter("name"))):
            a.append(str(athlete))
        return "\n".join(a)

    def worst(self):
        a = sorted(self.d.values(), key = operator.attrgetter("total"))
        return str(a[-1])

    def best(self):
        a = sorted(self.d.values(), key = operator.attrgetter("total"))
        return str(a[0])






