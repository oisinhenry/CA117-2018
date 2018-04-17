class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{}, {}".format(self.x, self.y)

    def midpoint(self, other):
        midx = self.x / 2 + other.x / 2
        midy = self.y / 2 + other.y / 2
        return Point(midx, midy)



class Circle(object):

    def __init__(self, centre=0, radius=0):
        self.radius = radius
        self.centre = centre

    def __str__(self):
        return "Centre: ({})\nRadius: {}".format(self.centre, self.radius)

    def __add__(self, other):
        rnew = self.radius + other.radius
        cnew = Point.midpoint(self.centre, other.centre)
        return Circle(cnew, rnew)



# from circle_081 import Point, Circle

# def main():
#     p1 = Point()
#     p2 = Point(4,6)
#     c1 = Circle(p1, 10)
#     c2 = Circle(p2, 5)
#     c3 = c1 + c2
#     print(c3)

#     p3 = Point(10,10)
#     print("p3: {}".format(p3))
#     c4 = Circle(p3,15)
#     print("c4: {}".format(c4))
#     c5 = c2 + c4
#     print(c5)
    
# if __name__ == '__main__':
#     main()



