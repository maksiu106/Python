#!/usr/bin/env python3
#coding=utf-8

def factorial(n):
	result = 1
	for i in range (1, n+1): result *= i
	return result
	
argument = int(input("Dla jakiej liczby chcesz obliczyć silnię?\n"))
print(factorial(argument))
