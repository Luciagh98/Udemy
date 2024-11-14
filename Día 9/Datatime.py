#Manipular el tiempo, almacenar horas y fechas en variables...

import datetime

#Se manejan con 24 horas,minutos, segundos...Si no asignas valores, da resultado 0.
mi_hora = datetime.time(17,35)
print(type(mi_hora)) #<class 'datetime.time'>
print(mi_hora) #17:35:00

#Podemos añadir más datos.
mi_hora = datetime.time(17,35,50,1500)

#Para FECHAS
mi_fecha = datetime.datetime(2025,10,17)
print(mi_fecha) #2025-10-17 00:00:00

#Si solo queremos el AÑO:
print(mi_fecha.year) #2025

#Si queremos el nombre del dia o otro formato
print(mi_fecha.ctime()) #Fri Oct 17 00:00:00 2025

#Muestra la fecha de HOY, no modifica la fecha anterior, sinó que sirve para obtener el dia actual
print(mi_fecha.today()) #2024-04-24 15:40:22.626616

from datetime import datetime

mi_fecha = datetime(2025,5,15,22,10,15,2500)
print(mi_fecha) #2025-05-15 22:10:15.002500

#Modiicar un dato, en este caso, el mes:
mi_fecha = mi_fecha.replace(month = 11)
print(mi_fecha) #2025-11-15 22:10:15.002500

from datetime import date

nacimiento = datetime(1995,3,5)
defuncion = datetime(2095,6,19)

#Podemos hacer una diferencia de tiempos:
vida = defuncion - nacimiento
print(vida) #36631 days, 0:00:00
print(vida.days) #36631

from datetime import datetime

#Podemos saber la diferencia de tiempos:
despierta = datetime(2022,10,5,7,30)
duerme = datetime(2022,10,5,23,45)

vigilia = duerme - despierta
print(vigilia) #16:15:00