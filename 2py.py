Y = int(input())

if (Y % 4 == 0 and Y % 100 != 0) or Y % 400:
	print ('True')
else:
	print ('False')