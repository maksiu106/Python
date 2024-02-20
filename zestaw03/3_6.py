#!/usr/bin/env python3
#coding=utf-8

a = int(input("Wprowadź długość pierwszego boku prostokąta\n"))
b = int(input("Wprowadź długość drugiego boku prostokąta\n"))

napis = ""

for j in range(b):
	for i in range(a): napis += "+---"
	napis += "+\n"
	for i in range(a): napis += "|   "
	napis += "|\n"
	
for i in range(a): napis += "+---"
napis += "+\n"

print(napis)
