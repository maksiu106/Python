#!/usr/bin/env python3
#coding=utf-8

#kod jest poprawny i zadziała, ale parę rzeczy jest niepotrzebnych, a mianowicie średniki na końcach wyrażeń. Po ich usunięciu:
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y
    
#podany kod wymaga rozbicia na dwie linie tekstu - po dwukropku może wystąpić jedynie prosta instrukcja. Poprawniej:
for i in "axby":
	if ord(i) < 100: print (i)
	
#wyrażnie jest poprawne
for i in "axby": print (ord(i) if ord(i) < 100 else i)
