class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    def __str__(self):
        return "({:.1f}, {:.1f})".format(self.x, self.y)


class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        midx = (self.p1.x + self.p2.x)/2
        midy = (self.p1.y + self.p2.y)/2
        return Point(midx, midy)

    def length(self):
        return distance(self.p1, self.p2)


class Circle(object):

    def __init__(self, centre, radius):
        self.radius = radius
        self.centre = centre

    def overlaps(self, other):
        return self.centre.distance(other.centre) < self.radius + other.radius









