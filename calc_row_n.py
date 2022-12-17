#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  calc_row_n.py
#  
#  Copyright 2022 mike <mike@pop-os>
#
'''  
	Using entry in Wikipedia calc the coefficients in row n of Pascals Triangle
	Row 0 = 1
	Row 1 = 1 1
	Row 10 = 1 10 45 120 210 252 210 120 45 10 1  # 11 terms
	Generally:
		(10 0) = 1 where n = 10 and 0<=k<=10
		
		(n k) = (n k-1) * (n+1-k)	#recursive formula
'''

def row_coeff(n):
	# No Sanity Checks
	coeff = [1]
	k = 1
	if n%2 == 0: # n is even, n+1 terms
		while k < (n/2)+1:
			t1 = coeff[-1] * (n + 1 - k) // k
			coeff.append(t1)
			k += 1
		print(f"n:{n}  {coeff}")
	else:		# n is odd, n terms
		while k < (n+1)/2:
			t1 = coeff[-1] * (n + 1 - k) // k
			coeff.append(t1)
			k += 1
		print(f"n:{n}  {coeff}")
	return coeff
	
def kth_coeff(n,k):
	# No_Sanity_checks
	# Return the kth_coeff of row n
	# Note: k is zero based so k(3) returns the 4th term in the row
	
	# if k > n/2 - return the symmetrical coeff
	# breakpoint()
	
	if k > n/2:
		target = n - k + 1
	else:
		target = k + 1
	coeff = 1
	j = 1
	while j != target:
		coeff = coeff * (n + 1 - j) // j
		j += 1
	return coeff
		

def main(args):
	#row_coeff(8)
	#row_coeff(9)
	#row_coeff(10)
	#row_coeff(11)
	#row_coeff(20)
	
	#print(kth_coeff(10,5))
	#print(kth_coeff(10,6))
	#print(kth_coeff(10,7))
	
	print(kth_coeff(8,4))
	print(kth_coeff(10,6))
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
