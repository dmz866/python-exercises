from datetime import datetime, date, time

print(date(2025,11,28))
print(time(17, 35).minute)

mi_date = datetime(2026,12,1, 23, 11)
mi_date = mi_date.replace(month=5)
print(mi_date)

d = datetime.today()
print(d)




