'''
Ejemplo para ilustrar la imporetacion de la libreria datetime en Pyton 3 
Demuestra el uso de: hora, fecha y aritmetica de fechas
 '''
import datetime
import time
SEPARATOR = ("*" * 20)+"\n"
#Creacion de una hora especifica

Hora = datetime.time(10,20,30)
print (f"El tipo de pbjeto de la hora es {type(Hora)}")
print(f"La hora es{Hora}")
print(f"La hora de{Hora} es {Hora.hour}")#Limite 0..23
print(f"El minuto de{Hora} es {Hora.minute}")#Limite 0..59
print(f"La segundo de{Hora} es {Hora.second}")#Limite 0..59
print(f"La microsegundo de{Hora} es {Hora.microsecond}")#Limite 0..0

print(SEPARATOR * 2)

Pass
fecha_actual = datetime.date.today()
print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"la fecha actual es {fecha_actual}")
print(f"El ano actual es{fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El dia actual es {fecha_actual.day}")
print(SEPARATOR * 2)

#convertir un string a fecha
fecha_capturada = imput("dame una fecha (dd/mm/aaaa):\n")
fecha_procesada = imput("dame una fecha (dd/mm/aaaa):\n")
print(f"El tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"la fecha actual es {fecha_actual}")
print(f"El ano actual es{fecha_actual.year}")
print(f"El mes actual es {fecha_actual.month}")
print(f"El dia actual es {fecha_actual.day}")
print(SEPARATOR * 2)


print(f"El factorial de {valorNumerico} es igual a{math.factorial(valorNumerico)}")
potencia= int(input("dame un valor entero:\n"))
print(f"El resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)}")
print(SEPARATOR * 4)
Pass


print(f"El valor de Pi es {math.pi}")