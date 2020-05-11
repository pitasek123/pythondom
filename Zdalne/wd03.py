## ZADANIE 1 ##

A = [round(1/x, 3) for x in range(1,11)]
B = [2**x for x in range(11)]
C = [x for x in B if x % 4 == 0]

print(A)
print(B)
print(C)

## ZADANIE 2 ##

import numpy as np
a = np.arange(16).reshape(4,4)
print(a)
print("\n", np.diagonal(a))

# poszperalem troche w internecie i zrobilem takie rozwiazanie, nie jest do konca poprawne z poleceniem ale dziala :) #

## ZADANIE 3 ##

zakupy = {
    "mleko" : 'l',
    "jajka" : "szt",
    "ser" : "kg",
    "mieso" : "kg",
    "banan" : "szt"
}

a = [x for x,y in zakupy.items() if y == "szt"]
print(a)

## ZADANIE 4 ##
import math

def liniowa(a,b):
    if (a>0):
        print("Ta funkcja jest rosnaca!")
        return a,b
    elif (a<0):
        print("Ta funkcja jest malejaca!")
        return a,b
    else:
        print("Ta funkcja jest stala!")
        return a,b
print(liniowa(-1,2))
print(liniowa(3,5))
print(liniowa(0,3))

## ZADANIE 5 ##

def row_pros(a1,a2):
    if a1==a2:
        print("Proste sa rownolegle!")
        return a1,a2
    elif a1*a2==-1:
        print("Proste sa prostopadle!")
        return a1,a2
    else:
        print("Blad!")
print(row_pros(3,3))
print(row_pros(1,-1))

## ZADANIE 6 ##
import math

def row_okr(x=6,a=3,y=6,b=2):
    ((x-a)**2 + (y-b)**2)
    return math.sqrt((x-a)**2 + (y-b)**2)
print("Promien wynosi: ")
print(row_okr())

# ## ZADANIE 7 ##
import math

def pitagoras(a=6,b=8,c=0):
    c = math.sqrt(a**2 + b**2)
    return c
print(pitagoras())

## ZADANIE 8 ##
def suma_ciagu(a1 = 1, r = 1, n = 10):
    sum = (n / 2) * (2 * a1 + (n - 1) * r)
    return sum
print(suma_ciagu())

## ZADANIE 9 ##
def ciag(* liczby):
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn *= i
        return iloczyn
print(ciag())
print("Iloczyn ciagu dla podanych liczb wynosi: ")
print(ciag(1,2,3,4,5,6))

## ZADANIE 10 ##
def zakupy(** produkty):
    return sum(produkty.values())
print(zakupy(maslo = 2, mleko = 1, jajka = 4, banan = 6))




