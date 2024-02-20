#!/usr/bin/env python3
#coding=utf-8

list = [(1,2,5), [5,3], [1,120], (9,6,12,9,100), []]
final = []

for i in list:
	final.append(sum(i))

print("Wyjściowa lista: ", list)
print("Suma elementów każdej sekwencji na liście: ", final)
