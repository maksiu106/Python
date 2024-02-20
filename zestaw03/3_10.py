#!/usr/bin/env python3
#coding=utf-8

#najprostszy sposób inicjalizacji - jako pary klucz-wartość: dictionary = {"M": 1000, "D": 500, "C":100, "L":50, "X":10, "V":5, "I":1}
#inny sposób - lista krotek i użycie funkcji: dictionary = dict([("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)])
#jeszcze inny sposób - stworzenie pustej listy i dodanie po kolei elementów
dictionary = {}
dictionary['M'] = 1000
dictionary['D'] = 500
dictionary['C'] = 100
dictionary['L'] = 50
dictionary['X'] = 10
dictionary['V'] = 5
dictionary['I'] = 1

def roman2int(roman):
	number = 0
	next_val = 1
	for i in reversed(roman):
		if dictionary[i] >= next_val:
			number += dictionary[i]
			next_val = dictionary[i]
		else:
			number -= dictionary[i]
			next_val = dictionary[i]
	return number
	
roman = input("Wprowadź liczbę rzymską, którą program przekonwertuje na arabską\n")
arabic = roman2int(roman)
print(arabic)
