#!/usr/bin/env python3
#coding=utf-8

length = int(input("Wprowadź długość miarki, jaka ma zostać narysowana\n"))

napis = "|"
for i in range(length):
	napis += "....|"

napis += '\n0'
for i in range(length):
	napis += str(i+1).rjust(5)
	
print(napis)
