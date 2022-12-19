#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  coeff.py
#  
#  Copyright 2022 mike <mike@pop-os>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

from sympy import sieve, primefactors, primerange
from math import floor, factorial

def coeff(n,k):
	# No sanity checks
	# calc binomial coeff (n k)
	nlist = [(x) for x in range(n,k,-1)]
	n_klist = [(x) for x in range(n-k,1,-1)]
	#print(nlist)
	#print(n_klist)
	for j in range(len(n_klist)):	# divisors
		for i in range(len(nlist)):
			if n_klist[j]==1 or nlist[i]%n_klist[j]!=0:
				continue
			# found a divisor
			nlist[i] //= n_klist[j]
			n_klist[j] = 1
	print("First pass")
	print(nlist)
	print()
	print(n_klist)
	
	#second pass
	for j in range(len(n_klist)):	# divisors
		for i in range(len(nlist)):
			if n_klist[j]==1 or nlist[i]%n_klist[j]!=0:
				continue
			# found a divisor
			nlist[i] //= n_klist[j]
			n_klist[j] = 1
	print("Second pass")
	print(sorted(nlist))
	print()
	print(sorted(n_klist))
	# remove unity values from both lists
	nlist = sorted(nlist,reverse=True)
	n_klist = sorted(n_klist,reverse=True)
	
	nlist = sorted(nlist[0:nlist.index(1)],reverse=True)
	n_klist = sorted(n_klist[0:n_klist.index(1)],reverse=True)
	
	print("Pruned")
	print(nlist)
	print()
	print(n_klist)
	#  find and divide by prime factors
	
def legendre(n):
	# returns a list of tuples
	# tuple has number of times each prime factor of n appears in n!
	# for n = 200 prime factors are [2,5]
	# tuples are (5,49) (2,197)
	
	l_pf = primerange(n+1)
	
	lg = list()
	for prime in l_pf:
		pn = prime
		t = 0
		while pn <= n:
			t += floor(n / pn)
			pn *= prime
		lg.append((prime,t))
	return lg
	
def raisat_p2(n,r):
	# Reference Eureka.pdf Author Saisat Proposition 2
	prng = primerange(n+1)
	SumOfTerms = 0
	for p in prng:
		q = p
		t = 0
		while q <= n:
			t += floor(n/q) - floor(r/q) - floor((n-r)/q)
			q *= p
		if t > 0:
			SumOfTerms += p*t
			# print(f"({p},{t})")
			print('.',end="")
	print()
	return SumOfTerms

def main(args):
	print(raisat_p2(20000000,15000000))
	print()
	

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
