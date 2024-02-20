#!/usr/bin/env python3
#coding=utf-8

while True:
	value = input("Wprowadź liczbę, dla której chcesz policzyć trzecią potęgę. Aby zakończyć program, wpisz 'stop'\n")
	
	try: print(pow(float(value), 3))
	except ValueError:
		if (value == "stop"): break
		else: print("Wprowadziłeś coś innego niż liczbę")
