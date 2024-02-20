#!/usr/bin/env python3
#coding=utf-8

Sequence_1 = ('a', 'b', 'd', 't', 'z')
Sequence_2 = ('a', 'd', 'q', 'y', 'z')

Sequence_1 = set(Sequence_1)
Sequence_2 = set(Sequence_2)

same_elem = Sequence_1.intersection(Sequence_2)
all_elem = Sequence_1.union(Sequence_2)

print("Lista wspólnych elementów w sekwencjach: ", same_elem)
print("Lista wszystkich elementów w obu sekwencjach: ", all_elem)
