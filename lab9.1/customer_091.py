class Customer(object):

    discount = 0.0

    def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
        self.name = name
        self.balance = balance
        self.addr_line1 = addr_line1
        self.addr_line2 = addr_line2
        self.addr_line3 = addr_line3

    def __str__(self):
        a = []
        a.append(self.name)
        a.append(self.addr_line1)
        a.append(self.addr_line2)
        a.append(self.addr_line3)
        a.append("Balance: {:.2f}".format(self.balance))
        a.append("Discount: {:.0%}".format(self.discount))
        a.append("Amount due: {:.2f}".format(self.balance - self.balance * self.discount))
        return "\n".join(a)

    def owes(self):
        return self.balance - self.balance * self.discount







class ValuedCustomer(Customer):

    discount = 0.1





