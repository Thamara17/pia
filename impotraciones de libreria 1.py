'''Ejemplo para ilustrar la importacion de la likbreria random en Python 3 
Demuestra el uso de: randfrage (stop), randrange (start,stop,step),
 random (), choice(seq), shuffle (seq)'''

import random
from tkinter import SEPARATOR
from tkinter.ttk import Separator
SEPARATOR = ('*' * 20) + '\n'

print(f'obteniendo un numero entero aleatorio que puede ir del 0 al 19:{random.randrange(20)}')
print(SEPARATOR)
print(f'obteniendo un numero entero aleatorio par que puede ir del 2 al 20:{random.randrange(2,21,2)}')
print(SEPARATOR)
print(f'obteniendo un numerico entre 0.0 y1.0:{random.random()}')
print(SEPARATOR * 2)
 
listaDePrueba = [10, 20, 30, 40, 15, 25, 35, 45]
print(f'La lista de prurba es {listaDePrueba}')
print(f'El valor seleccionado aleatoriamente de la lista antyerior es {random.choice(listaDePrueba)}')
print(Separator)
random.shuffle(listaDePrueba)
print(f"La lista ya'perturbada\barajada' es{listaDePrueba}")+



