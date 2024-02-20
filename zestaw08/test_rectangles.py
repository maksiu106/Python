# Kod testujący moduł rectangles.py

from points import Point
from rectangles import Rectangle
import pytest

@pytest.fixture
def rectangles():
	r1 = Rectangle(0, 0, 4, 4)
	r2 = Rectangle(2, 1, 7, 6)
	r3 = Rectangle(0, 0, 4, 4)
	r4 = Rectangle(100, 100, 200, 200)
	return r1, r2, r3, r4
	
def test_raise_error():
	with pytest.raises(ValueError):
		Rectangle(2, 0, 1, -4)
	
def test_str(rectangles):
	r1, r2, r3, r4 = rectangles
	assert str(r1) == "[(0, 0), (4, 4)]"
	assert str(r2) == "[(2, 1), (7, 6)]"
	
def test_repr(rectangles):
	r1, r2, r3, r4 = rectangles
	assert repr(r1) == "Rectangle(0, 0, 4, 4)"
	assert repr(r2) == "Rectangle(2, 1, 7, 6)"
	
def test_eq(rectangles):
	r1, r2, r3, r4 = rectangles
	assert (r1 == r3) == True
	assert (r1 == r2) == False
	
def test_ne(rectangles):
	r1, r2, r3, r4 = rectangles
	assert (r1 != r3) == False
	assert (r1 != r2) == True
	
def test_center(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.center == Point(2,2)
	assert r2.center == Point(4.5,3.5)
	
def test_area(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.area() == 16
	assert r2.area() == 25
	
def test_move(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.move(2,5) == Rectangle(2,5,6,9)
	assert r2.move(-3,-1) == Rectangle(-1,0,4,5)
	
def test_intersection(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.intersection(r2) == Rectangle(2,1,4,4)
	assert r1.intersection(r3) == Rectangle(0,0,4,4)
	with pytest.raises(ValueError):
		r1.intersection(r4)

def test_cover(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.cover(r2) == Rectangle(0,0,7,6)
	assert r1.cover(r4) == Rectangle(0,0,200,200)
	
def test_make4(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.make4() == (Rectangle(0,2,2,4), Rectangle(2,2,4,4), Rectangle(0,0,2,2), Rectangle(2,0,4,2))
	
def test_from_points(rectangles):
	r1, r2, r3, r4 = rectangles
	assert Rectangle.from_points((Point(0,0),Point(4,4))) == r1
	assert Rectangle.from_points((Point(2,1),Point(7,6))) == r2
	
def test_top(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.top == 4
	assert r2.top == 6
	
def test_bottom(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.bottom == 0
	assert r2.bottom == 1
	
def test_left(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.left == 0
	assert r2.left == 2
	
def test_right(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.right == 4
	assert r2.right == 7
	
def test_width(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.width == 4
	assert r2.width == 5
	
def test_height(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.height == 4
	assert r2.height == 5
	
def test_topleft(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.topleft == Point(0,4)
	assert r2.topleft == Point(2,6)

def test_topright(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.topright == Point(4,4)
	assert r2.topright == Point(7,6)
	
def test_bottomleft(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.bottomleft == Point(0,0)
	assert r2.bottomleft == Point(2,1)
	
def test_bottomright(rectangles):
	r1, r2, r3, r4 = rectangles
	assert r1.bottomright == Point(4,0)
	assert r2.bottomright == Point(7,1)

if __name__ == '__main__':
	pytest.main()     # uruchamia wszystkie testy
	
