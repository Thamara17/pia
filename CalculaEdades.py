import datetime
SEPARATOR = "*" * 30
#Se desea capturar una lista de fechas de nacimiento (3) y se deberá informar cuantos 
#años cumplen esas personas en el año en curso

def calcula_edad(fecha_nac):
    hoy = datetime.date.today()
    return hoy.year - fecha_nac.year - ((hoy.month,hoy.day) < (fecha_nac.day))

    lista_fechas = []
for elementos in range(3):
    fecha_capturada= input("Dime una fecha(dd/mm/aaaa):\n")
    fecha_procrsada= datetime.datetime.strptime(fecha_capturada,"%d/%m/%Y").date()
    lista_fechas.append(fecha_procrsada)

print(SEPARATOR)

edades = list(map(calcula_edad, lista_fechas))

for edad in edades:
    print(edad)
    
