class Contact(object):

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):  # returns a string describing a contact's details
        return "{} {} {}".format(self.name, self.phone, self.email)


class ContactList(object):

    def __init__(self):
        self.d = {}     # mappings from names to contacts

    def add_contact(self, c):   # insert a new mapping from name to contacts
                                # c is an instance of Contact() with attributes
        self.d[c.name] = c      # mapping to an object not a primitive type

    def del_contact(self, name):
        if name in self.d:
            del self.d[name]

    def get_contact(self, name):
        if name in self.d:
            return self.d[name].__str__()   # directly invoke str method on contact object
        else:
            return "{} : No such contact".format(name)

    def __str__(self):  # string representation of entire list
        slist = []
        slist.append("Contact list")
        slist.append("------------")
        for k, v in sorted(self.d.items()):
            slist.append(v.__str__())
        return "\n".join(slist)





