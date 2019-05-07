#!/usr/bin/env python3

import Imaginary as im
import Matrice as mat
import numpy as np
import sys

var = {}

def find_num(expr):
	sign = 1
	val = 0.0
	frac = 0.1
	c = 0
	if (not len(expr)):
		raise ValueError
	if (expr[c] == '-'):
		sign = -1
		c += 1
	while (c != len(expr)):
		if (expr[c] >= '0' and expr[c] <= '9'):
			val *= 10
			val += (int(expr[c]) - int('0'))
		else:
			break
		c += 1
	if (not c != len(expr) or expr[c] != '.'):
		return ([sign * val, c])
	c += 1
	while (c != len(expr)):
		if (expr[c] >= '0' and expr[c] <= '9'):
			val += (int(expr[c]) - int('0')) * frac
			frac /= 10
		else:
			break
		c += 1
	return ([sign * val, c])

def find_unkn(expr):
	print(poulet)

def eval(expr, unkn = None):
	prev = expr
	val = find_num(expr)
	if (val[1] == 0):
		print("There are equal")
	print(im.Imaginary(val[0]))
	return(im.Imaginary(val[0]))


def parse_line(line):
	global var
	split = line.split("=")
	if (len(split) != 2):
		return (-1)
	right = split[0]
	left = split[1]
	right = right.replace(' ', '').replace('\t', '')
	left = left.replace(' ', '').replace('\t', '')
	if (left == "?"):
		if (right in var):
			print(var[right])
		else:
			print("No variable found")
	else:
		try:
			val = eval(left)
		except ValueError:
			return (-1)
		var[right] = val
	return (0)

def main():
	line = input('> ')
	while (line):
		if (parse_line(line) == -1):
			print("Invalid Input")
		line = input('> ')

if (__name__ == "__main__"):
	main()
