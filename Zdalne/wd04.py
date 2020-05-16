## ZADANIE 1 ##
plik = open("podzielne4","w")

A = [x for x in range(1,100) if x % 4 == 0]

A = ','.join([str(liczba) for liczba in A])
plik.writelines(A) ## --> Dziekuje za pomoc, od razu lepiej wyglada :)

plik = open("podzielne4","r")

print(plik.read())  

# ZADANIE 2 ##
plik = open("podzielne4","r")
print(plik.read())

## ZADANIE 3 ##
with open("piosenka.txt", "w") as plik:
    plik.write("Wlazl kotek na plotek\n")
    plik.write("I mruga")
    
plik = open("piosenka.txt" , "r")
print(plik.read())
plik.close()



    