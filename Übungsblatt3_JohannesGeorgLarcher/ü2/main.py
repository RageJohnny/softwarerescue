class Car(object):
    def __init__(self):
        self.number_of_tires = 4

    def addtire(self):

        if self.number_of_tires == 4:
            print("Hinzufügen nicht möglich!")
        else:
            self.number_of_tires += 1
            print("Reifen hinzugefügt")
            return self.number_of_tires

    def removetire(self):
        self.number_of_tires -= 1
        return self.number_of_tires

    def drive(self):
        if self.number_of_tires == 4:
            print("Ich geb Gas ich geb Gas")
        else:
            print("Du kannst erst losfahren wenn du genügend Reifen montiert hast!")


class Motorbike(Car):
    def __init__(self):
        super().__init__()
        self.number_of_tires = 2

    def addtire(self):

        if self.number_of_tires == 2:
            print("Hinzufügen nicht möglich!")
        else:
            self.number_of_tires += 1
            print("Reifen hinzugefügt")
            return self.number_of_tires

    def drive(self):
        if self.number_of_tires == 2:
            print("Ich geb Gas ich geb Gas")
        else:
            print("Du kannst erst losfahren wenn du genügend Reifen montiert hast!")


class Truck(Car):
    def __init__(self):
        super().__init__()
        self.number_of_tires = 6

    def addtire(self):

        if self.number_of_tires == 6:
            print("Hinzufügen nicht möglich!")
        else:
            self.number_of_tires += 1
            print("Reifen hinzugefügt")
            return self.number_of_tires

    def drive(self):
        if self.number_of_tires == 6:
            print("Ich geb Gas ich geb Gas")
        else:
            print("Du kannst erst losfahren wenn du genügend Reifen montiert hast!")


c = Car()
b = Motorbike()
t = Truck()
print(c.addtire())
print(c.removetire())
c.drive()
print(b.addtire())
print(b.removetire())
print(t.addtire())
print(t.removetire())
print(t.addtire())
t.drive()
