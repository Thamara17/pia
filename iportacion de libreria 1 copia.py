'''Ejemplo para ilustrar la importacion de la likbreria random en Python 3 
Demuestra el uso de: randfrage (stop), randrange (start,stop,step),
 random (), choice(seq), shuffle (seq)'''

import random
from tkinter import SEPARATOR
from tkinter.ttk import Separator
SEPARATOR = ('*' * 24) + '\n'

print(f'obteniendo un numero entero aleatorio que puede ir del 0 al 14:{random.randrange(24)}')
print(SEPARATOR)
print(f'obteniendo un numero entero aleatorio par que puede ir del 2 al 24:{random.randrange(2,21,2)}')
print(SEPARATOR)
print(f'obteniendo un numerico entre 0.5 y1.5:{random.random()}')
print(SEPARATOR * 2)
 
listaDePrueba = [5, 10, 15, 20, 90, 100, 110, 120]
print(f'La lista de prurba es {listaDePrueba}')
print(f'El valor seleccionado aleatoriamente de la lista antyerior es {random.choice(listaDePrueba)}')
print(Separator)
random.shuffle(listaDePrueba)
print(f"La lista ya'perturbada\barajada' es{listaDePrueba}")
