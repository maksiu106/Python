#!/usr/bin/env python3
#coding=utf-8

line = '''Stworzyłem ultradługi performance eskalujący radyklanie'''
print("Napis wyjsciowy: ", line)
line = line.split()
result=""
for i  in line: result=result+i[0]
print("Wynik dzialania: ", result)