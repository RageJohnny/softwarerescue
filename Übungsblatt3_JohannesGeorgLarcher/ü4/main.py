import os

os.system("cls")

class gameboard():
    def __init__(self):
        self.spaces = [" "," "," "," "," "," "," "," "," "," "]

    def printboard(self):
        print(" %s | %s | %s " %(self.spaces[1],self.spaces[2],self.spaces[3]))
        print("____________")
        print(" %s | %s | %s " %(self.spaces[4],self.spaces[5],self.spaces[6]))
        print("____________")
        print(" %s | %s | %s " %(self.spaces[7],self.spaces[8],self.spaces[9]))

    def refresh(self, zellenNo, player):
        if self.spaces[zellenNo] == " ":
            self.spaces[zellenNo] = player

    def ist_gewinner(self, player):
            if  self.spaces[1] == player and self.spaces[2]==player and self.spaces[3] == player:
                return True
            if  self.spaces[4] == player and self.spaces[5]==player and self.spaces[6] == player:
                return True
            if  self.spaces[7] == player and self.spaces[8]==player and self.spaces[9] == player:
                return True
            if  self.spaces[1] == player and self.spaces[4]==player and self.spaces[7] == player:
                return True
            if  self.spaces[2] == player and self.spaces[5]==player and self.spaces[8] == player:
                return True
            if  self.spaces[3] == player and self.spaces[6]==player and self.spaces[9] == player:
                return True
            if  self.spaces[1] == player and self.spaces[5]==player and self.spaces[9] == player:
                return True
            if  self.spaces[3] == player and self.spaces[5]==player and self.spaces[7] == player:
                return True
            return False

    def draw(self):
           uses_spaces = 0
           for spaces in self.spaces:
               if spaces != " ":
                   uses_spaces +=1
           if uses_spaces ==9:
               return True
           else:
               return False



    def restart(self):
        self.spaces = [" "," "," "," "," "," "," "," "," "," "]



gameboard = gameboard()
gameboard.printboard()


def print_header():
    print("Welcome to Bobs Tic Tac Toe")

def refresh_spielbrett():
    os.system("cls")
    print_header()
    gameboard.printboard()

refresh_spielbrett()

while True:
    refresh_spielbrett()

    x_choice = int(input("\n Enter 1 - 9 please: "))

    gameboard.refresh(x_choice,"X")

    refresh_spielbrett()

    if gameboard.ist_gewinner("X"):
        print("X Wins")
        play_again= input("Play Again J/N ").upper()
        if play_again== "J":
            gameboard.restart()
            continue
        else:
            break

    if gameboard.draw():
        print("Unentschieden!")
        play_again= input("Play Again J/N ").upper()
        if play_again== "J":
            gameboard.restart()
            continue
        else:
            break




    O_choice = int(input("\nO) Enter 1 - 9 please:  "))

    gameboard.refresh(O_choice,"O")

    if gameboard.ist_gewinner("O"):
       print("O Wins")
       play_again= input("Play Again J/N ").upper()
       if play_again== "J":
           gameboard.restart()
           continue
       else:
           break






