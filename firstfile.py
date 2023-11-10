#!/usr/bin/env python

print("Hello World")


word = '*'
def count():
	i = 0
	while i < 100000:
		print(word)
		word = word + '*'
		i += 1
len(word)