from random import randint
zahl = randint(1, 100)
# Ratespiel


print("Hi, Lass und ein Speil spielen ! :D ")
print("")
print("Rate eine Zahl zwischen 1 und 100")

versuche = 0

while True:
    try:
        versuch = int(input("Rate eine Zahl: "))
    except ValueError:
        print("Bitte gib eine gültige Zahl ein!")
        continue

    versuche += 1

    if versuch == zahl:
        print(f"Richtig geraten! Du hast {versuche} Versuche Gebraucht.")
        break
    elif versuch <= zahl:
        print("Die Zahl ist zu klein")
    else:
        print("Die Zahl ist zu groß!")


