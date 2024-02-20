#!/usr/bin/env python3
#coding=utf-8

def i_odwracanie(L, left, right):
	while left<right:
		L[right], L[left] = L[left], L[right]
		right-=1
		left+=1
	
def r_odwracanie(L, left, right):
	if left<right:
		L[right], L[left] = L[left], L[right]
		r_odwracanie(L, left+1, right-1)

argument = [1,3,7,5,6,3,2,10,120]
print("Lista wyjściowa: ", argument)

i_odwracanie(argument, 1, 7)
print("Lista odwrócona iteracyjnie w zakresie 1-7: ", argument)

argument = [1,3,7,5,6,3,2,10,120]
list_rec = r_odwracanie(argument, 2, 5)
print("Lista odwrócona rekuruencyjnie w zakresie 2-5: ", argument)
