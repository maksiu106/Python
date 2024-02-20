#!/usr/bin/env python3
#coding=utf-8

import math

class Point:
	"""Klasa reprezentująca punkty na płaszczyźnie."""

	def __init__(self, x, y):  # konstuktor
		self.x = x
		self.y = y

	def __str__(self): # zwraca string "(x, y)"
		return "(" + str(self.x) + ", " + str(self.y) + ")"

	def __repr__(self): # zwraca string "Point(x, y)"
		return "Point(" + str(self.x) + ", " + str(self.y) + ")"

	def __eq__(self, other): # obsługa point1 == point2
		return (self.x == other.x and self.y == other.y)

	def __ne__(self, other): # obsługa point1 != point2
        	return not self == other

	# Punkty jako wektory 2D.
	def __add__(self, other): # v1 + v2
		return Point(self.x + other.x, self.y + other.y)

	def __sub__(self, other): # v1 - v2
		return Point(self.x - other.x, self.y - other.y)

	def __mul__(self, other): # v1 * v2, iloczyn skalarny, zwraca liczbę
		return self.x*other.x + self.y*other.y

	def cross(self, other): # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
		return self.x * other.y - self.y * other.x

	def length(self): # długość wektora
		return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2))

	def __hash__(self):
		return hash((self.x, self.y))   # bazujemy na tuple, immutable points
		
# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase):

	def setUp(self):
		self.p1 = Point(2,5)
		self.p2 = Point(4,9)
		self.p3 = Point(2,5)
	
	def test_str(self):
		self.assertEqual(str(self.p1), "(2, 5)")
		self.assertEqual(str(self.p2), "(4, 9)")
		
	def test_repr(self):
		self.assertEqual(repr(self.p1), "Point(2, 5)")
		self.assertEqual(repr(self.p2), "Point(4, 9)")
		
	def test_eq(self):
		self.assertTrue(self.p1 == self.p3)
		self.assertFalse(self.p1 == self.p2)
	
	def test_ne(self):
		self.assertFalse(self.p1 != self.p3)
		self.assertTrue(self.p1 != self.p2)
		
	def test_add(self):
		self.assertEqual(self.p1+self.p2, Point(6, 14))
		self.assertEqual(self.p1+self.p3, Point(4, 10))
		
	def test_sub(self):
		self.assertEqual(self.p1-self.p2, Point(-2, -4))
		self.assertEqual(self.p2-self.p1, Point(2, 4))
		
	def test_mul(self):
		self.assertEqual(self.p1*self.p2, 53)
		self.assertEqual(self.p1*self.p1, 29)
		
	def test_cross(self):
		self.assertEqual(self.p1.cross(self.p2), -2)
		self.assertEqual(self.p2.cross(self.p1), 2)
		self.assertEqual(self.p1.cross(self.p1), 0)
		
	def test_length(self):
		self.assertEqual(self.p1.length(), math.sqrt(29))
		self.assertEqual(self.p2.length(), math.sqrt(97))
		
	def test_hash(self):
		self.assertEqual(hash(self.p1), hash((2, 5)))
		self.assertEqual(hash(self.p2), hash((4, 9)))
		
	def tearDown(self): pass
		

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy

