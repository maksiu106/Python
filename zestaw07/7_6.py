#!/usr/bin/env python3
#coding=utf-8

import random

class Iterator_A:
	def __init__(self):
		self.n = 0

	def __iter__(self):
		return self
		
	def __next__(self):
		temp = self.n
		self.n = (self.n+1)%2
		return temp
		
class Iterator_B:
	def __init__(self):
		self.dictionary = {0: "N", 1: "E", 2: "S", 3: "W"}
		self.n = self.dictionary[random.randint(0,3)]
		
	def __iter__(self):
		return self
	
	def __next__(self):
		temp = self.n
		self.n = self.dictionary[random.randint(0,3)]
		return temp
		
class Iterator_C:
	def __init__(self):
		self.n = 0
	
	def __iter__(self):
		return self
		
	def __next__(self):
		temp = self.n
		self.n = ((self.n) + 1) % 7
		return temp
		
print("Działanie iteratora zwracającego na przemian ciąg zer i jedynek: ")
it = Iterator_A()
for i in range(10):
	print(next(it))
	
print("\nDziałanie iteratora zwracającego losowe kierunki geograficzne: ")
it = Iterator_B()
for i in range(10):
	print(next(it))
	
print("\nDziałanie iteratora zwracającego numery kolejnych dni tygodnia: ")
it = Iterator_C()
for i in range(10):
	print(next(it))
	
	
