#!/usr/bin/env python3
#coding=utf-8

import sys

def kadane1d(arr):
	global_max = local_max = float('-inf')
	start = end = temp_start = temp_end = 0
	
	for i in range(len(arr)):
		#sprawdzanie lokalnego maksimum
		if (arr[i] > local_max+arr[i]):
			local_max = arr[i]
			temp_start = i
		else:
			local_max += arr[i]
			
		temp_end = i
		
		#sprawdzanie globalnego maksimum
		if (local_max > global_max):
			global_max = local_max
			start = temp_start
			end = temp_end
		elif (arr[i] == 0):
			end = temp_end
			
	return global_max, start, end
	
def kadane2d(matrix):
	rows = len(matrix)
	columns = len(matrix[0])
	global_max = float('-inf')
	top = bottom = right = left = 0
	

	for i in range(rows):
		temp = [0] * columns #tworzenie tymczasowego wiersza

		for j in range(i, rows):
			for k in range(columns):
				temp[k] += matrix[j][k] #w każdej komórce jest suma danego elementu oraz wszystkich powyżej niego licząc od indeksu i

			#algorytm Kadane 1D na tablicy temp
			local_max = float('-inf')
			temp_start = 0

			for k in range(columns):
				#sprawdzanie lokalnego maksimum
				if (temp[k] > temp[k] + local_max):
					local_max = temp[k]
					temp_start = k
				else:
					local_max += temp[k]

				#sprawdzanie globalnego maksimum
				if (local_max > global_max):
					global_max = local_max
					top = i
					bottom = j
					left = temp_start
					right = k

	return global_max, top, bottom, left, right
	
def print_matrix(A):
	for row in A:
		print(row)
		
def print_submatrix(A, top, bottom, left, right):
	for row in A[top:bottom+1]:
		print(row[left:right+1])
	
def main():
	if len(sys.argv) == 1: input = "in.txt"
	else: input = sys.argv[1]
	
	with open(input, 'r') as file:
		text = file.readlines()
		
	matrix = []
	for line in text:
		row = list(map(float, line.strip().split()))
		matrix.append(row)
		
	if len(matrix) == 1:
		# Dane są jednowymiarowe
		matrix = matrix[0]
		print("Tablica jednowymiarowa:", matrix)
		print("\nWywołanie algorytmu Kadane dla tablicy jednowymiarowej")
		suma, start, end = kadane1d(matrix)
		print("Maksymalna suma elementów podmacierzy: ", suma)
		print("Początkowy indeks: ", start, "; końcowy indeks: ", end)
		print("\nOstateczny kształt podtablicy o największej sumie elementów:")
		print(matrix[start:end+1])
	else:
		# Dane są dwuwymiarowe
		print("Macierz dwuwymiarowa:")
		print_matrix(matrix)
		print("\nWywołanie algorytmu Kadane dla macierzy dwuwymiarowej")
		suma, top, bottom, left, right = kadane2d(matrix)
		print("Maksymalna suma elementów podmacierzy: ", suma)
		print("Lewy indek początku: ", left, "; prawy indeks końca: ", right)
		print("Górny indeks początku: ", top, "; dolny indeks końca: ", bottom)
		print("\nOstateczny kształt podmacierzy o największej sumie elementów:")
		print_submatrix(matrix, top, bottom, left, right)
	
if __name__ == "__main__":
	main()
