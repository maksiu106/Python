#!/usr/bin/env python3
#coding=utf-8

from points import Point

class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie."""

	def __init__(self, x1, y1, x2, y2):
		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self): # "[(x1, y1), (x2, y2)]"
		return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

	def __repr__(self): # "Rectangle(x1, y1, x2, y2)"
		return "Rectangle(" + str(self.pt1.x) + ", " + str(self.pt1.y) + ", " + str(self.pt2.x) + ", " + str(self.pt2.y) + ")"

	def __eq__(self, other): # obsługa rect1 == rect2
		return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)
		
	def __ne__(self, other): # obsługa rect1 != rect2
		return not self == other

	def center(self): # zwraca środek prostokąta
		return Point((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)

	def area(self): # pole powierzchni
		return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

	def move(self, x, y): # przesunięcie o (x, y)
		self.pt1.x += x
		self.pt2.x += x
		self.pt1.y += y
		self.pt2.y += y
		return self

# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):

	def setUp(self):
		self.r1 = Rectangle(0, 0, 4, 4)
		self.r2 = Rectangle(2, 1, 7, 6)
		self.r3 = Rectangle(0, 0, 4, 4)
		
	def test_str(self):
		self.assertEqual(str(self.r1), "[(0, 0), (4, 4)]")
		self.assertEqual(str(self.r2), "[(2, 1), (7, 6)]")
		
	def test_repr(self):
		self.assertEqual(repr(self.r1), "Rectangle(0, 0, 4, 4)")
		self.assertEqual(repr(self.r2), "Rectangle(2, 1, 7, 6)")
		
	def test_eq(self):
		self.assertTrue(self.r1 == self.r3)
		self.assertFalse(self.r1 == self.r2)
		
	def test_ne(self):
		self.assertFalse(self.r1 != self.r3)
		self.assertTrue(self.r1 != self.r2)
		
	def test_center(self):
		self.assertEqual(self.r1.center(), Point(2,2))
		self.assertEqual(self.r2.center(), Point(4.5,3.5))
		
	def test_area(self):
		self.assertEqual(self.r1.area(), 16)
		self.assertEqual(self.r2.area(), 25)
		
	def test_move(self):
		self.assertEqual(self.r1.move(2,5), Rectangle(2,5,6,9))
		self.assertEqual(self.r2.move(-3,-1), Rectangle(-1,0,4,5))
	
	def tearDown(self): pass
		

if __name__ == '__main__':
	unittest.main()     # uruchamia wszystkie testy

