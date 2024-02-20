#!/usr/bin/env python3
#coding=utf-8

#kod niepoprawny: L = [3, 5, 4] ; L = L.sort()
#Funkcja sort sortuje listę L i nie zwraca niczego, więc nie da się wyniku jej działania przypisać do czegokolwiek
#kod poprawny:
L = [3, 5, 4] ; L.sort()

#kod niepoprawny: x, y = 1, 2, 3
#za mało zmiennych, za dużo wartości, które próbuje się im przypisać
#kod poprawny (przykład):
x, y, z = 1, 2, 3

#kod niepoprawny: X = 1, 2, 3 ; X[1] = 4
#Krotka jest strukturą danych, której nie da się zmienić; próba zastąpienia w niej jednej wartości inną jest więc niemożliwa

#kod niepoprawny: X = [1, 2, 3] ; X[3] = 4
#Lista ma tylko trzy elementy; nie zmieni się więc elementu o indeksie 3 (a więc de facto czwartego w niej elementu)
#kod poprawny (przykładowy):
X = [1, 2, 3] ; X[2] = 4

#kod niepoprawny: X = "abc" ; X.append("d")
#nie istnieje metoda append dla stringa. Żeby jej użyć, trzeba zdefiniować X jako listę, albo:
#kod poprawny (przykład):
X = "abc" ; X += 'd'

#kod niepoprawny: L = list(map(pow, range(8)))
#Funkcja pow potrzebuje więcej niż jednego argumentu. Co więcej, wymogi pozostałych funkcji wymagają, żeby te argumenty były iterowalne
#kod poprawny (przykład):
L = list(map(pow, range(4), range(8)))
