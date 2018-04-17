class BankAccount(object):

    next_account_number = 16555232
    total_lodgements = 0
    interest_rate = 0.043

    def __init__(self, forename, surname, balance=0.00): 
        self.surname = surname
        self.forename = forename
        self.balance = balance
        self.account_number = BankAccount.next_account_number
        BankAccount.next_account_number += 1

    def lodge(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1

    def apply_interest(self):
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest

    def __iadd__(self, amount):
        self.balance += amount
        BankAccount.total_lodgements += 1
        return self

    def __str__(self):
        a = []
        name = self.forename + " " + self.surname
        a.append("Name: {}".format(name))
        
        a.append("Account number: {:d}".format(self.account_number))
        a.append("Balance: {:.2f}".format(self.balance))
        return "\n".join(a)








