import random as r

def mergeSort(alist):

    #Splitten der Liste
   if len(alist)>1:
       mid = len(alist)//2
       lefthalf = alist[:mid]
       righthalf = alist[mid:]

    #Funktionsaufruf der Rekursion
       mergeSort(lefthalf)
       mergeSort(righthalf)

    #Festlegen der Indexe für die Listen der Seiten
       i=0
       j=0
       k=0

    #Festlegen der while-Schleifen
       while i < len(lefthalf) and j < len(righthalf):
           if lefthalf[i] < righthalf[j]:
               alist[k]=lefthalf[i]
               i=i+1
           else:
               alist[k]=righthalf[j]
               j=j+1
           k=k+1

       while i < len(lefthalf):
           alist[k]=lefthalf[i]
           i=i+1
           k=k+1

       while j < len(righthalf):
           alist[k]=righthalf[j]
           j=j+1
           k=k+1

list_sort=[]

#Generieren einer Liste mit 10 Zufallszahlen
for i in range (10):
   list_sort.append(r.randrange(1, 101, 1))
print (list_sort)
mergeSort(list_sort)
print(list_sort)