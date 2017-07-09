#! /usr/bin/python

#Wywolywanie funkcji za pomoca skryptu

import testerwroc
import sys,os

plik=open("lorem.txt")
for linia in plik:
	z=testerwroc.podziel_na_slowa(linia)
	# print z,
	if "bash" in z:
		print linia

print os.path.exists("lorem.txt")
a=testerwroc.czy_jest_liczba("13")
if a:
	print "Wpisana przez Ciebie jest liczba" 

	

