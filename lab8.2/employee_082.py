class Employee(object):

    next_employee_number = 0

    def __init__(self, name, hourly_rate=9.25, hours_worked=0):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        a = []
        a.append("Name: {:s}".format(self.name))
        a.append("ID: {:d}".format(self.employee_number))
        a.append("Hours: {:.2f}".format(self.hours_worked))
        a.append("Rate: {:.2f}".format(self.hourly_rate))
        a.append("Wages: {:.2f}".format(self.hourly_rate * self.hours_worked))
        return "\n".join(a)

    def add_hours(self, hours):
        self.hours_worked = float(self.hours_worked)
        self.hours_worked += float(hours)