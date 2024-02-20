#!/usr/bin/env python3
#coding=utf-8

L = [10, 50, 12, 4]
print("Lista przed złożeniem: ", L)

word = "".join(str(i) for i in L)
print("Lista po złożeniu: ", word)
