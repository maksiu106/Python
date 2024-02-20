#!/usr/bin/env python3
#coding=utf-8

line = "Abrakadabra szukamy najdłuższego wyrazu"
print("Wyjściowy napis: ", line)

line=line.split()
index_max=0

for i in range(len(line)):
    if (len(line[i]) > len(line[index_max])): index_max = i

print("Najdłuższy wyraz: ", line[index_max])
print("Jego długość: ", len(line[index_max]))
