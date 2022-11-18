import pandas as pd
import random

SEPARADOR = ("*" * 20) + "\n"

diccionario_notas = {"Crecencio":[87,100, None],"Domitila":[80, None,57], \
                     "Rutilio":[80, 70,57], "Panfilo":[20,100,100], "Ludoviko":[100,100,100]}
notas_diccionario = pd.DataFrame(diccionario_notas)
print(notas_diccionario)
print(SEPARADOR)
