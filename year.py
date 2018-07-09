from datetime import date

def get_age():
    age = int(input("Enter the year you were born: "))
    dat2 = date.today()
    return dat2.year - age

print(get_age(), " years old")