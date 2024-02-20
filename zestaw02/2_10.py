#!/usr/bin/env python3
#coding=utf-8

line = '''Jest to napis wielowierszowy.
Ma spacje i tabulacje
oraz newliney'''
print("\nNapis wygląda:\n", line)

line = line.split()
print("\nLiczba slow w napisie: ", len(line))