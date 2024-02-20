#!/usr/bin/env python3
#coding=utf-8

line = "jest to napis złożony z wyrazów które zaraz zostaną posortowane na dwa sposoby"
print("Wyjściowy napis: ", line)

line = line.split()
line = sorted(line)
line = " ".join(line)
print("\nAlfabetycznie: ", line)

line = line.split()
line = sorted(line, key=len,)
line = " ".join(line)
print("\nDługościowo: ", line)
