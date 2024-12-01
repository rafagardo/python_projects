# import datetime
from datetime import datetime, date

# mi_hora = datetime.time(2, 30, 45)
# print(type(mi_hora))
# print(mi_hora.hour)
#
# mi_dia = datetime.date(2020, 12, 31)
# print(mi_dia.year)
# print(mi_dia.month)
# print(mi_dia.day)
# print(mi_dia.ctime())
# print(mi_dia.today())

mi_fecha = datetime(2020, 12, 31, 2, 30, 45)
mi_fecha = mi_fecha.replace(year=2025)
print(mi_fecha)

nacimiento = date(1980, 1, 1)
defuncion = date(2080, 12, 31)
vida = defuncion - nacimiento
print(vida.days)

despierta = datetime(2020, 12, 31, 7, 30, 0)
duerme = datetime(2020, 12, 31, 23, 30, 0)
vigilia = duerme - despierta
print(vigilia)
print(vigilia.seconds)