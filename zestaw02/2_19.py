#!/usr/bin/env python3
#coding=utf-8

L = [2, 17, 128, 341, 1, 43, 45]
print("przed: ", L)

for i in range(len(L)):
	L[i] = str(L[i])
	L[i] = L[i].zfill(3)

print("po: ", L)
