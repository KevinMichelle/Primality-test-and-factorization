import sys
import math

def factorizar(n):
	factores = []
	if n > 1:
		for i in xrange(2, n + 1):
			while n % i == 0:
				n = n / i
				factores.append(i)
			if n == 1:
				break
	elif n == 1:
		factores.append(n)
	return factores

if len(sys.argv) != 2:
	print 'El numero de argumentos es invalido'
else:
	isnumber = True
	ispositive = True
	for i in xrange(1, len(sys.argv)): # Desde sys.argv[1] hasta sys.argv[len(sys.argv) - 1]
		if not sys.argv[i].isdigit(): # Si alguno de los argumentos no son numeros
			isnumber = False
			break
		elif not int(sys.argv[i]) > 0: # Si alguno de los argumento (numeros) no son mayores que 0
			ispositive = False # Si alguno de los argumentos que si son numeros no son mayores que cero
			break
	if isnumber and ispositive:
		n = int(sys.argv[1])
		factores = factorizar(n)
		print factores
	else:
		print 'Todos los argumentos deben ser numeros enteros mayores que 0'
