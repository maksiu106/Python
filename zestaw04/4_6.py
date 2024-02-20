#!/usr/bin/env python3
#coding=utf-8

def sum_seq(sequence):
	result = 0
	for item in sequence:
		if isinstance(item, (list, tuple)): result += sum_seq(item)
		else: result += item
	return result
	
seq = [1,(2,3),[],[4,(5,6,7)],8,[9], 500, (2, 200, 98)]
print("Zadana sekwencja: ", seq)
print("Suma wszystkich liczb w sekwencjach w sekwencjach w tej sekwencji wynosi: ", sum_seq(seq))
