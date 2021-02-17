print("Hallo mein Name ist Bob. Wie ist Ihr Name?")
name = input(">>")
print("Schoenen guten Tag " + name)
print("Welches Trennzeichen möchten Sie verwenden?")
limiter = input(">>")
print("Bitte Text zum Trennen eingeben!")
entrystring = input(">> ")



def letter_spacing(user_input, delimiter=" "):
    return delimiter.join(user_input)

test = entrystring
result = letter_spacing(test, limiter)

print(result)
