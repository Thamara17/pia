from xml.dom.minidom import Element
import numpy as np
import random
SEPARATOR = ("*" * 20) + "\n"

#Comprobacion de que un array de numpy y una lista no poseen el mismo comportamiento:
#Una lista puede contener elementos de diferente tipo de dato
#en una array de numpy todos los elementos son del miso tipo de datos

list =[10, 'abc', 20]
print(lista)
print([type(Element) for element in list])
print(SEPARATOR)
