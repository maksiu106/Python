#!/usr/bin/env python3
#coding=utf-8

def make_ruler(n):
	napis = "|"
	for i in range(n):
		napis += "....|"

	napis += '\n0'
	for i in range(n):
		napis += str(i+1).rjust(5)
		
	return napis
	
def make_grid(cols, rows):
	napis = ""

	for j in range(rows):
		for i in range(cols): napis += "+---"
		napis += "+\n"
		for i in range(cols): napis += "|   "
		napis += "|\n"
	
	for i in range(cols): napis += "+---"
	napis += "+\n"
	
	return napis
	
length = int(input("Wprowadź długość miarki, jaka ma zostać narysowana\n"))
print(make_ruler(length))

a = int(input("Wprowadź długość pierwszego boku prostokąta\n"))
b = int(input("Wprowadź długość drugiego boku prostokąta\n"))
print(make_grid(a, b))
