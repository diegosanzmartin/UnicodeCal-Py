import sys
import calendar

# Crear el calendario de un año específico,
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
year = 2022
calendar_data = cal.yeardatescalendar(year)

index = []
result = "     "
mycal = [[],[],[],[],[],[],[]]
weekdays = ['   ', 'Mon', '   ', 'Wed', '   ', 'Fri', '   ']
months = ['Ja', 'Fe', 'Mr', 'Ap', 'My', 'Jn', 'Jl', 'Au', 'Se', 'Oc', 'Nv', 'De']
cont = 1

# Imprimir cada fila del calendario
for dates in calendar_data:
    for week in dates:
        for i, day in enumerate(week):
            years = [d.year for d in day]
            month = [d.month for d in day]
            days = [d.day for d in day]
            
            if month[0] == 12 and len(index) == 0:
                index.append(1)
            else:
                index.append(month[0])

            for x, m in enumerate(mycal):
                if years[x] == year-1 or years[x] == year+1:
                    m.append("  ")
                else:
                    m.append("⬛")

counts = [index.count(i) for i in range(1, 13)]

for i, count in enumerate(counts):
    result += months[i] + "  " * (count-1)

print(result)

for i, w in enumerate(mycal):
    print(weekdays[i] + "  " + ''.join(w))
