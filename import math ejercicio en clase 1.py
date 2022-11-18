from ast import Pass
import math
from tkinter import SEPARATOR
SEPARATOR = ("*" * 10)+"\n"
'''
Ejemplo para ilustrar la imporetacion de la libreria math en Pyton 3 
Demuestra el uso de: floor(x), trunc (x), ceil(x), round(x), factorial(x), pow(x,y),sqrt(x) y pi
 '''
valorflotante = float (input("introduce un valor con fraccion decimal:\n"))
print (f"El siguiente entero hacia arriba de {valorflotante} es {math.ceil(valorflotante)}")
print(SEPARATOR)
print(f"El siguiente entero hacia abajo de {valorflotante}es {math.floor(valorflotante)}")
print(SEPARATOR)
print (f"la parte entera truncada de {valorflotante} es {math.trunc(valorflotante)}") # Equivalente
print(SEPARATOR * 5)
Pass
valorNumerico = int(input("dame un valor entero:\n"))
print(f"La raiz cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARATOR)
print(f"El factorial de {valorNumerico} es igual a{math.factorial(valorNumerico)}")
potencia= int(input("dame un valor entero:\n"))
print(f"El resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARATOR * 4)
Pass


print(f"El valor de Pi es {math.pi}")

