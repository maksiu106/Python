#!/usr/bin/env python3
#coding=utf-8

from points import Point

class Rectangle:
	"""Klasa reprezentująca prostokąt na płaszczyźnie."""

	def __init__(self, x1, y1, x2, y2):
		if (x1 > x2): raise ValueError("x1 should have a smaller value than x2")
		elif (y1 > y2): raise ValueError("y1 should have a smaller value than y2")
		
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

	def area(self): # pole powierzchni
		return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

	def move(self, x, y): # przesunięcie o (x, y)
		self.pt1.x += x
		self.pt2.x += x
		self.pt1.y += y
		self.pt2.y += y
		return self
		
	def intersection(self, other): # część wspólna prostokątów
		if (self.pt2.x < other.pt1.x or self.pt2.y < other.pt1.y): raise ValueError("Those rectangles don't cover each other")
		return Rectangle(other.pt1.x, other.pt1.y, self.pt2.x, self.pt2.y)
		
	def cover(self, other): # prostąkąt nakrywający oba
		if (self.pt1.x < other.pt1.x): x1 = self.pt1.x
		else: x1 = other.pt1.x
		
		if (self.pt1.y < other.pt1.y): y1 = self.pt1.y
		else: y1 = other.pt1.y
		
		if (self.pt2.x > other.pt2.x): x2 = self.pt2.x
		else: x2 = other.pt2.x
		
		if (self.pt2.y > other.pt2.y): y2 = self.pt2.y
		else: y2 = other.pt2.y
		
		return Rectangle(x1,y1,x2,y2)

	def make4(self): # zwraca krotkę czterech mniejszych
		first = Rectangle(self.pt1.x, (self.pt2.y + self.pt1.y)/2, (self.pt2.x + self.pt1.x)/2, self.pt2.y)
		second = Rectangle((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2, self.pt2.x, self.pt2.y)
		third = Rectangle(self.pt1.x, self.pt1.y, (self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)
		fourth = Rectangle((self.pt2.x + self.pt1.x)/2, self.pt1.y, self.pt2.x, (self.pt2.y + self.pt1.y)/2)
		
		return (first, second, third, fourth)
		
	@classmethod
	def from_points(klasa, points): #stworzy prostokąt z krotki dwóch punktów
		point1, point2 = points
		return klasa(point1.x, point1.y, point2.x, point2.y)
		
	@property
	def center(self): # zwraca środek prostokąta
		return Point((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)
		
	@property
	def top(self):
		return self.pt2.y
		
	@property
	def bottom(self):
		return self.pt1.y
		
	@property
	def left(self):
		return self.pt1.x
		
	@property
	def right(self):
		return self.pt2.x
		
	@property
	def width(self):
		return (self.pt2.x-self.pt1.x)
		
	@property
	def height(self):
		return (self.pt2.y-self.pt1.y)
		
	@property
	def topleft(self):
		return Point(self.pt1.x, self.pt2.y)
		
	@property
	def topright(self):
		return Point(self.pt2.x, self.pt2.y)
		
	@property
	def bottomleft(self):
		return Point(self.pt1.x, self.pt1.y)
		
	@property
	def bottomright(self):
		return Point(self.pt2.x, self.pt1.y)
		
