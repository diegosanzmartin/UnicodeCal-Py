import calendar
import datetime
import json
import sys

def get_unicode(year, month, day):
    # Abrir archivo JSON
    with open(sys.argv[1], 'r') as f:
        numeros = json.load(f)

    fecha = datetime.date(year, month, day)

    # Obtener número del día especificado
    num = numeros.get(str(fecha.timetuple().tm_yday))

    # Asociar número con icono
    if num == None:
        return "  "
    elif num == 0:
        return '⬛'
    elif num <= 2:
        return '⬜'
    elif num <= 3:
        return '🟨'
    elif num <= 9:
        return '🟧'
    elif num >= 10:
        return '🟥'
    else:
        return "ER"

def create_year_calendar(year):
    cal = calendar.Calendar(firstweekday=calendar.SUNDAY)
    calendar_data = cal.yeardatescalendar(year)
    return calendar_data

def generate_month_index(calendar_data):
    index = []
    ctrl = []
    for dates in calendar_data:
        for week in dates:
            for i, day in enumerate(week):
                years = [d.year for d in day]
                month = [d.month for d in day]
                days = [d.day for d in day]

                if month[0] == 12 and len(index) == 0:
                    ctrl = days
                    index.append(1)
                elif ctrl == days:
                    pass
                else:
                    ctrl = days
                    index.append(month[0])
    return index

def generate_month_counts(index):
    counts = [index.count(i) for i in range(1, 13)]
    return counts

def generate_month_string(counts):
    result = "     "
    months = ['Ja', 'Fe', 'Mr', 'Ap', 'My', 'Jn', 'Jl', 'Au', 'Se', 'Oc', 'Nv', 'De']
    for i, count in enumerate(counts):
        result += months[i] + "  " * (count-1)
    return result

def generate_weekday_strings(calendar_data, year):
    mycal = [[],[],[],[],[],[],[]]
    weekdays = ['   ', 'Mon', '   ', 'Wed', '   ', 'Fri', '   ']
    index = []
    ctrl = []
    for dates in calendar_data:
        for week in dates:
            for i, day in enumerate(week):
                years = [d.year for d in day]
                month = [d.month for d in day]
                days = [d.day for d in day]

                for x, m in enumerate(mycal):
                    if years[x] == year-1 or years[x] == year+1:
                        m.append("  ")
                    elif x == 0 and ctrl == days:
                        break
                    else:
                        ctrl = days
                        m.append(get_unicode(years[x],month[x],days[x]))

    return mycal, weekdays

def print_calendar(year, result, mycal, weekdays):
    print(result)
    for i, w in enumerate(mycal):
        print(weekdays[i] + "  " + ''.join(w))

# Crear el calendario de un año específico
year = 2023
calendar_data = create_year_calendar(year)

# Generar el índice de los meses
index = generate_month_index(calendar_data)

# Generar los conteos de los días en cada mes
counts = generate_month_counts(index)

# Generar la cadena de caracteres con los meses
result = generate_month_string(counts)

# Generar las cadenas de caracteres para los días de la semana
mycal, weekdays = generate_weekday_strings(calendar_data, year)

# Imprimir el calendario
print_calendar(year, result, mycal, weekdays)
