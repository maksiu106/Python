#!/usr/bin/env python3
#coding=utf-8

from math import gcd

# funkcja sprawiająca, że ułamek jest skrócony, a minus jest zawsze w liczniku
def simplify(frac):
	if frac[0] == 0: #jeśli licznik to 0, mianownik będzie równy 1
		frac[1] = 1
		return
	if frac[1] < 0: #jeśli mianownik jest ujemny, przesuwamy minus do licznika
		frac[1] = -frac[1]
		frac[0] = -frac[0]
	nwd = gcd(frac[0], frac[1]) #skracamy ułamek
	frac[0] = int(frac[0]/nwd)
	frac[1] = int(frac[1]/nwd)
	return


# frac1 + frac2
def add_frac(frac1, frac2):
	result = [0,0]
	result[1] = frac1[1] * frac2[1] #liczenie wspólnego mianownika
	result[0] = frac1[0]*frac2[1] + frac2[0]*frac1[1]
	simplify(result)
	return result

# frac1 - frac2
def sub_frac(frac1, frac2):
	result = [0,0]
	result[1] = frac1[1] * frac2[1] #liczenie wspólnego mianownika
	result[0] = frac1[0]*frac2[1] - frac2[0]*frac1[1]
	simplify(result)
	return result

# frac1 * frac2
def mul_frac(frac1, frac2):
	result = [0,0]
	result[0] = frac1[0] * frac2[0]
	result[1] = frac1[1] * frac2[1]
	simplify(result)
	return result

# frac1 / frac2
def div_frac(frac1, frac2):
	result = [0,0]
	result[0] = frac1[0] * frac2[1]
	result[1] = frac1[1] * frac2[0]
	simplify(result)
	return result

# bool, czy dodatni
def is_positive(frac):
	simplify(frac)
	if (frac[0]>=0): return True
	else: return False

# bool, typu [0, x]
def is_zero(frac):
	if (frac[0] == 0): return True
	else: return False

# -1 | 0 | +1
def cmp_frac(frac1, frac2):
	float1 = frac1[0]/frac1[1]
	float2 = frac2[0]/frac2[1]
	if (float1 > float2): return 1
	elif (float1 == float2): return 0
	else: return -1
	
# konwersja do float
def frac2float(frac):
	return float(frac[0]/frac[1])

import unittest

class TestFractions(unittest.TestCase):

	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual(add_frac([1,2], [1,3]), [5,6])

	def test_sub_frac(self):
		self.assertEqual(sub_frac([-1,5], [1,7]), [-12,35])

	def test_mul_frac(self):
		self.assertEqual(mul_frac([1,-6], [-2,3]), [1,9])
		
	def test_div_frac(self):
		self.assertEqual(div_frac([1,-6], [-3,2]), [1,9])

	def test_is_positive(self):
		self.assertTrue(is_positive([1,9]))
		self.assertFalse(is_positive([1,-9]))

	def test_is_zero(self):
		self.assertTrue(is_zero([0,125]), True)
		self.assertFalse(is_zero([10,9]), False)

	def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1,9], [8,9]), -1)
		self.assertEqual(cmp_frac([1,9], [1,9]), 0)
		self.assertEqual(cmp_frac([1,9], [8,-9]), 1)

	def test_frac2float(self):
		self.assertEqual(frac2float([1,20]), 0.05)

	def tearDown(self): pass
		

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy
