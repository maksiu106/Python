#!/usr/bin/env python3
#coding=utf-8

def fibonacci(n):
	if (n==0): return 0
	elif (n==1): return 1
	else:
		last1 = 0
		last2 = 1
		for i in range (2, n+1):
			result = last1 + last2
			last1 = last2
			last2 = result
		return result
	
argument = int(input("Wprowadź wartość, dla której chcesz obliczyć liczbę Fibonacciego\n"))
print(fibonacci(argument))
