#!/usr/bin/env python3



'''

Jako argument bere procento AT, projde soubor a vypíše sekvence s procentem AT vyšším než je zadané procento.

u5_delka.py -p50

'''

import sys



def chyba_zadání():

	print("Použití: {} [-pN] ( N = požadované procento AT mezi 0 a 100)".format(sys.argv[0]))

	sys.exit()

	

if len(sys.argv) == 1:

	print('Nezadali jste žádný argument!')

	chyba_zadání()

elif len(sys.argv) == 2:

	argument = sys.argv[1]

	if argument.startswith('-p'):

		try:

			procento = int(argument[2:])

		except ValueError:

			print('Neznámý tvar argumentu!', argument, '!')

			chyba_zadání()

	else:

		print('Neznámý tvar argumentu!', argument, '!')

		chyba_zadání()

	if procento not in range(0, 101, 1):

		print ('Zadané číslo', procento, 'není procento!')

		chyba_zadání()

else:

	print('Zadali jste větší počet argumentů než skript požaduje!')

	chyba_zadání()

		

výstup = ''

	

with open ('sekvence.txt', encoding='utf-8') as soubor:

	for radka in soubor:

		radka = radka.upper()

		procento_GC = (radka.count('A') + radka.count('T')) / (len(radka) - 1)

		if procento_GC * 100 > procento:

			výstup += radka

		

if výstup == '':

	print('Nenalezena žádná sekvence splňující zadaný parametr.')

else:

	print(výstup)

		

#with open('vystup_procento.txt', mode='w', encoding='utf-8') as soubor_out:	

	#soubor_out.write(výstup)

	
