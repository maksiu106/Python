# Kod testujący program kadane.py

from kadane import kadane1d, kadane2d
import pytest

#testy dla Kadane 2D

def test_1():
	matrix = [
		[-1, -1, -1, -1, -1, -1],
		[-2, 2, 2, 3, 4, -1],
		[-2, -1, 2, 4, -5, 1],
		[0, -1, -1, -1, -1, -1]]
	assert kadane2d(matrix) == (12, 1, 2, 1, 3)
	
def test_2():
	matrix = [
		[-1, 0, -2],
		[-5, -10, -3],
		[-2, -7, -5]]
	assert kadane2d(matrix) == (0, 0, 0, 1, 1)
	
def test_3():
	matrix = [
		[5, 5, 5, 0],
		[-2, -2, -2, -2],
		[3, 3, 3, 1]]
	assert kadane2d(matrix) == (18, 0, 2, 0, 2)
	
def test_4():
	matrix = [
		[1, 1, 1, 1, 1],
		[1, 1, 1, 1, 1]]
	assert kadane2d(matrix) == (10, 0, 1, 0, 4)
	
def test_5():
	matrix = [
		[-5, -5, -5, -5],
		[-5, 2, 2, -5],
		[-5, 0, -1, -5],
		[-5, 2, 0, -5]]
	assert kadane2d(matrix) == (5, 1, 3, 1, 2)
	
def test_6():
	matrix = [
		[-20, -5],
		[-5, -2]]
	assert kadane2d(matrix) == (-2, 1, 1, 1, 1)
	
def test_7():
	matrix = [
		[-1, -1, -1, -1],
		[-1, 0, 10, -1],
		[-1, 10, 0, -1],
		[-1, -1, -1, -1]]
	assert kadane2d(matrix) == (20, 1, 2, 1, 2)
	
def test_8():
	matrix = [
		[1, 2, -5, -5],
		[1, 2, -5, -5],
		[-5, -5, -5, -5]]
	assert kadane2d(matrix) == (6, 0, 1, 0, 1)
	
def test_9():
	matrix = [
		[-5, -5, 1, 2],
		[-5, -5, 1, 2],
		[-5, -5, -5, -5]]
	assert kadane2d(matrix) == (6, 0, 1, 2, 3)
	
def test_10():
	matrix = [
		[-5, -5, -5, -5],
		[1, 2, -5, -5],
		[1, 2, -5, -5]]
	assert kadane2d(matrix) == (6, 1, 2, 0, 1)
	
def test_11():
	matrix = [
		[-5, -5, -5, -5],
		[-5, -5, 1, 2],
		[-5, -5, 1, 2]]
	assert kadane2d(matrix) == (6, 1, 2, 2, 3)
	
def test_12():
	matrix = [
		[20, 20, -5, -5],
		[-5, -5, 20, 20]]
	assert kadane2d(matrix) == (60, 0, 1, 0, 3)
		
	
#testy dla Kadane 1D

def test_13():
	array = [-7, -8, -7, -7, -2, -5]
	assert kadane1d(array) == (-2, 4, 4)
	
def test_14():
	array = [-1, -1, 2, -1, 2, -1, 2, -1, 2, -5, -10]
	assert kadane1d(array) == (5, 2, 8)
	
def test_15():
	array = [-10, -10, -10, 5, 0, -10]
	assert kadane1d(array) == (5, 3, 4)
	
def test_16():
	array = [1, 1, 1, 1, 1]
	assert kadane1d(array) == (5, 0, 4)
	
def test_17():
	array = [-2, -2, -2, 5, 0, -2, 4, -10]
	assert kadane1d(array) == (7, 3, 6)
		

if __name__ == '__main__':
	pytest.main()     # uruchamia wszystkie testy
	
