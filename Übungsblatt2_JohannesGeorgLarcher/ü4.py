#Mathematische Formel zur Berechnung des Pascalschen Dreiecks:
#Im Prinzip ist das Pascalsche Dreieck die Darstellung der Binomialkoeffizienten.
#Es ergibt sich also, dass der untergeordnete Wert die Summe der darübergeordneten Elemente ist.


list1 = [[1]]
list2 = []
count = 0
print("Hallo mein Name ist Bob! \nIch werde heute ihr Pascalsches Dreieck erstellen!")
print("Bitte Anzahl der Zeilen eingeben!")
rows = int(input(">> "))

while count != rows:

    for i in range(rows - 1):

        for j in range(len(list1[i]) + 1):

            if 1 <= j <= len(list1[i]) - 1:
                number = list1[i][j - 1] + list1[i][j]
                list2.append(number)
            else:
                list2.append(1)

        if list2 not in list1:
            list1.append(list2)

        list2 = []

    count += 1

bige = len(str(max(list1[-1]))) #Auslesen des größten Wertes der Liste
lastrow = ' '.join([str(eintrag).center(bige) for eintrag in list1[-1]]) #Auslesen der letzten Zeile

for i in list1:
    print(' '.join([str(eintrag).center(bige) for eintrag in i]).center(len(lastrow))) #Ausgabe des Dreiecks