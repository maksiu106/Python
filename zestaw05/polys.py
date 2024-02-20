#!/usr/bin/env python3
#coding=utf-8

#funkcja konwertująca wielomiany, aby ich listy miały taką samą długość
def convert(poly1, poly2):
	while len(poly1) > len(poly2):
		poly2.append(0)
	while len(poly2) > len(poly1):
		poly1.append(0)
	return

#funkcja usuwa niepotrzebne zera z końca listy wielomianowej
def standarize(poly):
	while (poly and poly[len(poly)-1] == 0):
		poly.pop()
	return

# poly1(x) + poly2(x)
def add_poly(poly1, poly2):
	result = []
	convert(poly1, poly2)
	for i in range (len(poly1)):
		result.append(poly1[i]+poly2[i])
	standarize(result)
	return result

# poly1(x) - poly2(x)
def sub_poly(poly1, poly2):
	result = []
	przeniesienie = 0
	convert(poly1, poly2)
	for i in range (len(poly1)):
		result.append(poly1[i]-poly2[i])
	standarize(result)
	return result

# poly1(x) * poly2(x)
def mul_poly(poly1, poly2):
	result = [0]*(len(poly1)+len(poly2))
	for i in range (len(poly1)):
		for j in range(len(poly2)):
			result[i+j] += poly1[i]*poly2[j]
	standarize(result)
	return result
	
# bool, [0], [0,0], itp.
def is_zero(poly):
	for i in range (len(poly)):
		if poly[i] != 0: return False
	return True

# bool, porównywanie poly1(x) == poly2(x)
def eq_poly(poly1, poly2):
	convert(poly1, poly2)
	for i in range (len(poly1)):
		if (poly1[i] != poly2[i]): return False
	return True

# poly(x0), algorytm Hornera
def eval_poly(poly, x0):
	result = 0
	for i in reversed(poly):
		result = result*x0 + i
	return result

# poly1(poly2(x)), trudne!
def combine_poly(poly1, poly2):
	convert(poly1, poly2)
	result = []
	for i in range (len(poly1)):
		result = add_poly(result, mul_poly(pow_poly(poly2, i), [poly1[i]]))
	standarize(result)
	return result

# poly(x) ** n
def pow_poly(poly, n):
	if (n==0): return [1]
	elif (n==1): return poly
	else:
		result = poly
		for i in range (n-1):
			result = mul_poly(result, poly)
		standarize(result)
		return result

# pochodna wielomianu
def diff_poly(poly):
	result = [0]*(len(poly)-1)
	for i in range (len(result)):
		result[i] = poly[i+1] * (i+1)
	standarize(result)
	return result

import unittest

class TestPolynomials(unittest.TestCase):

	def setUp(self):
		self.p1 = [0, 1]      # W(x) = x
		self.p2 = [0, 0, 1]   # W(x) = x^2
		self.p3 = [5, 12, 7, 0, 9]
		self.p4 = [0, 7, 0, 12, 0, 51]

	def test_add_poly(self):
		self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
		self.assertEqual(add_poly(self.p1, self.p3), [5, 13, 7, 0, 9])
		self.assertEqual(add_poly(self.p3, self.p4), [5, 19, 7, 12, 9, 51])

	def test_sub_poly(self):
		self.assertEqual(sub_poly(self.p3, self.p4), [5, 5, 7, -12, 9, -51])
		self.assertEqual(sub_poly(self.p4, self.p3), [-5, -5, -7, 12, -9, 51])

	def test_mul_poly(self):
		self.assertEqual(mul_poly(self.p3, self.p4), [0, 35, 84, 109, 144, 402, 612, 465, 0, 459])
		self.assertEqual(mul_poly(self.p2, self.p4), [0, 0, 0, 7, 0, 12, 0, 51])

	def test_is_zero(self):
		self.assertTrue(is_zero([0,0,0,0,0]))
		self.assertFalse(is_zero(self.p4))

	def test_eq_poly(self):
		self.assertTrue(eq_poly(self.p3, [5, 12, 7, 0, 9]))
		self.assertFalse(eq_poly(self.p3, [5, 12, 1004, 0, 9]))

	def test_eval_poly(self):
		self.assertEqual(eval_poly(self.p2, 7), 49)
		self.assertEqual(eval_poly(self.p3, 3), 833)

	def test_combine_poly(self):
		self.assertEqual(combine_poly(self.p3, self.p2), [5, 0, 12, 0, 7, 0, 0, 0, 9])
		self.assertEqual(combine_poly(self.p2, self.p3), [25, 120, 214, 168, 139, 216, 126, 0, 81])

	def test_pow_poly(self):
		self.assertEqual(pow_poly(self.p3, 3), [125, 900, 2685, 4248, 4434, 5004, 6121, 4536, 2538, 2916, 1701, 0, 729])
		self.assertEqual(pow_poly(self.p2, 4), [0, 0, 0, 0, 0, 0, 0, 0, 1])

	def test_diff_poly(self):
		self.assertEqual(diff_poly(self.p3), [12, 14, 0, 36])
		self.assertEqual(diff_poly(self.p4), [7, 0, 36, 0, 255])

	def tearDown(self): pass

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy
