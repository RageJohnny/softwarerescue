from article import Article
import os
class Warehouse:
    def __init__(self):
        self.run = True
        self.spaces = {
            "a1": None,
            "a2": None,
            "a3": None,
            "b1": None,
            "b2": None,
            "b3": None
        }
        self.weight = 0
        self.occupied = 0
        self.available = 6
        self.status = None

    def add_article(self, place, article):
        print("add article", article.name)
        if self.spaces[place]:
            self.status = "The choosen space is already taken!"
        else:
            self.spaces[place] = article

    def remove_article(self, place):
        if (self.spaces[place]):
            self.spaces[place] = None

    def calculate_current_weight_and_stock(self):
        weight = 0
        occupied = 0
        for _, v in self.spaces.items():
            if (v):
                weight = weight + v.weight
                occupied = occupied + 1
        self.weight = weight
        self.occupied = occupied
        self.available = 6 - occupied

    def next_tick(self):
        userInput = input(
            "(a) to add, (r) to remove and (e) to exit: ")
        if (userInput == "a"):
            if (self.available == 0):
                self.status = "Stock is full! Not able to add new item!"
            else:
                name = input("Name of your article? ")
                weight = float(
                    input("Weight of your article?"))
                place = input("On which Space should i put your item?")
                article = Article(name, weight)
                self.add_article(place, article)
        if (userInput == "r"):
            place = input("Which space should i empty")
            self.remove_article(place)
        if (userInput == "e"):
            self.run = False

    def print_current_stock(self):
        for k in self.spaces.keys():
            if (self.spaces[k]):
                print(k, ":", self.spaces[k].name)
            else:
                print(k, ": Empty")

    def print_status(self):
        self.calculate_current_weight_and_stock()
        print("Available Spaces: ", self.available)
        print("Occupied Spaces: ", self.occupied)
        print("Total Weight: ", self.weight)
        if (self.status):
            print("")
            print(self.status)
            print("")
            self.status = None

    def start(self):
        while self.run:
            os.system("cls")
            print("Hello my name is Bob! I'm your personal warehouse assistent!")
            self.print_current_stock()
            print("")
            self.print_status()
            self.next_tick()
