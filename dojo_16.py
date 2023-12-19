# Time conversion

# the_input = input("Enter time in 12 hour format: ")

st = "12:01:00PM"


def timeConversion(s):
    time_part, period = s[:-2], s[-2:]

    # Convertir l'heure en composantes heure, minute, seconde
    hours, minutes, seconds = map(int, time_part.split(":"))

    # Convertir les heures PM (sauf 12 PM) en format 24 heures
    if period == "PM" and hours != 12:
        hours += 12
    # Convertir 12 AM en 00 heures
    elif period == "AM" and hours == 12:
        hours = 0

    # Formater l'heure convertie en format 24 heures
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


print(timeConversion(st))
