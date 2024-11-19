class P_Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getPerson(self):
        print(self.name + " has " + str(self.age) + " year")
