#!/usr/bin/env python3
#coding=utf-8

line = "Długi napis, dla którego sprawdzimy łączną ilość znaków."
print("Napis: ", line)

line=line.split()

result = sum(len(i) for i in line)

print("Łączna długość wyrazów: ", result)