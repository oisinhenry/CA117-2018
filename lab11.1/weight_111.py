
class Weight(object):

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.p = int(pounds)
        self.o = int(ounces)

    def from_ounces(num):
        pounds = num // Weight.OUNCES_PER_POUND
        ounces = num % Weight.OUNCES_PER_POUND
        return Weight(pounds, ounces)

    def total_ounces(self):
        return (self.p * 16) + self.o

    def __add__(self, other):
        return Weight.from_ounces(self.total_ounces() + other.total_ounces())

    def __iadd__(self, other):
        new = Weight.from_ounces(self.total_ounces() + other.total_ounces())
        self.p, self.o = new.p, new.o
        return self

    def __mul__(self, num):
        return Weight.from_ounces(self.total_ounces() * int(num))

    def __ne__(self, other):
        return self.total_ounces() != other.total_ounces()

    def __eq__(self, other):
        return self.total_ounces() == other.total_ounces()

    def __lt__(self, other):
        return self.total_ounces() < other.total_ounces()

    def __gt__(self, other):
        return self.total_ounces() > other.total_ounces()

    def __ge__(self, other):
        return self.total_ounces() >= other.total_ounces()

    def __str__(self):
        return('{} pound(s) and {} ounce(s)'.format(self.p, self.o)) 