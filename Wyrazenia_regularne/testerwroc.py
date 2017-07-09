#Funkcje pomocnie - wyrazenia regularne

import re  # import modulu wyrazen regularnych

def czy_jest_liczba(s):
 return re.match('[0-9]+',s)
	
def podziel_na_slowa(s):
 return s.split()
