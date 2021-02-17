import random as r

list = []

for i in range (10):
   list.append(r.randrange(1, 101, 1))
print("Unsortierte Liste: ", list)

def bubblesort(list):

    x = len(list)
    counter = 0

    for i in range (x):
        for j in range(x-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                counter+=1

    print("Sortierte Liste: ", list)
    print("Anzahl der Durchläufe: ", counter)


bubblesort(list)



