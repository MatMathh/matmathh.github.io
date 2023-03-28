from os import *
from math import *
from timeit import default_timer

def verificar_si_es_primo(numero: int)->str:
	inicio = default_timer()
	respuesta = "Es primo"
	if (numero == 0 or numero == 1 or numero == 4):
		respuesta = "No es primo"
	x = 2
	contador = 1
	while (x <= numero):
		if ((numero % x) == 0):
			respuesta = "No es primo"
			x = numero
		x = x + 1
		contador = contador + 1
	if (x == (numero + 1)):
		respuesta = "Es primo"
	final = default_timer()
	return str(respuesta + " y se ha tardado " + str(final - inicio) + " segundos en verificar, habiendo realizado " + str(contador) + " divisiones.")

print("Bienvenido a la verificadora de numeros primos")
numero = int(input("Por favor digite el número al cuál quiere verificar si es primo: "))
resultado = verificar_si_es_primo(numero)
print(resultado)