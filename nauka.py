# Manipulacja stringami
# x = "Ala ma kota, a kot ma Alę :3"

# y = x[0:3] przedział znaków od do (:)
# y = x[0:6]

# print(x)
# print(y)

# Instrukcje warunkowe

# x = int(input("Podaj liczbe: "))

# if x >= 5:
    # print("Zgadza się!")
# else:
    # print("Nie zgadza się!")

# print("Gotowe!")

# Instrukcja warunkowe cd.

imie = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")
wiek = int(input("Podaj swój wiek: "))
cena = int(input("Podaj cenę depilatora: "))

print("Witaj {imie}".format(imie=imie))
print("Twoje nazwisko to {nazwisko}".format(nazwisko=nazwisko))
print("Masz {wiek} lat!".format(wiek=wiek))

if cena >= 500:
    print("Chyba cię pogrzało, {cena} za depilator!?".format(cena=cena))

else:
    print("No za {cena} tyle to jeszcze ujdzie!".format(cena=cena))



