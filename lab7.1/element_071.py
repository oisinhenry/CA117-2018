class Element(object):

    def __init__(self, number, name, symbol, boiling_point):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.boiling_point = boiling_point

    def print_details(self):
        print("Number: {}\nName: {}\nSymbol: {}\nBoiling point: {} K".format(self.number, self.name, self.symbol, self.boiling_point))