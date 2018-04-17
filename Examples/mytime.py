# Model a time with a class
class Time(object):

    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def set_time(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = second

    def time_to_seconds(self):
        return self.hour * 60 * 60 + self.minute * 60 + self.second

    def __gt__(self, other):
        # returns True if self is greater than other - otherwise False
        return self.time_to_seconds() > other.time_to_seconds()

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def show_time(self):
        print("Time is: {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second))

    def plus(self, other):
        return seconds_to_time(self.time_to_seconds() + other.time_to_seconds())

    def __eq__(self, other):
        return (self.hour, self.minute, self.second == other.hour, other.minute, other.second)

    @classmethod    # can be invoked without an existing instance of the class
    def seconds_to_time(cls, s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        return cls(hour, minute, second)




