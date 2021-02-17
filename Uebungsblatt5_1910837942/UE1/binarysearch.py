def binary_search(list, value):
    first = 0
    last = len(list) - 1
    status ="-1"
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if list[mid] == value:
            found = True
            status ="Wert gefunden"
        else:
            if value < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found, status


print(binary_search([1, 2, 3, 5, 8, 16, 23, 24, 30, 45, 60], 6))
print(binary_search([1, 2, 3, 5, 8, 16, 23, 24, 30, 45, 60], 5))