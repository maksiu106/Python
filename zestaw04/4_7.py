#!/usr/bin/env python3
#coding=utf-8

def flatten(sequence):
	result = []
	for item in sequence:
		if isinstance(item, (list, tuple)): result += flatten(item)
		else: result.append(item)
	return result
	
seq = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("Zadana sekwencja, którą program spłaszczy: ", seq)
print("Sekwencja po spłaszczeniu: ", flatten(seq))
