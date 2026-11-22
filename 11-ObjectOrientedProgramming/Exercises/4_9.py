###
# Employee: text representation of an object
#
class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        text = self.surname + self.name[0] + str(self.seniority)
        if self.age >= 18:
            return text.upper()
        return text.lower()

print('C("Anna","May",17,7) returns', C("Anna", "May", 17, 7))
print('C("George","Brown",21,4) returns', C("George", "Brown", 21, 4))
