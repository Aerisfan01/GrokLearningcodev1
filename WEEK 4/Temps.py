temperatures = {'Beijing': 26.7, 'Mumbai': 27.6, 'Tokyo': 25.0, 'Seoul': 24.9, 'Bangkok': 29.0, 'Ho Chi Minh City': 27.5, 'Vienna': 20.8, 'Brussels': 18.4, 'Helsinki': 17.8, 'Berlin': 20.3, 'Rome': 24.1, 'Amsterdam': 17.6, 'Edinburgh': 15.3, 'Istanbul': 22.9, 'Nassau': 27.9, 'Ottawa': 21.2, 'Nuuk': 6.5, 'Mexico City': 18.2, 'Canberra': 5.7, 'Auckland': 10.9, 'Buenos Aires': 11.0, 'Rio de Janeiro': 21.3, 'Lima': 16.7, 'Cairo': 27.6, 'Nairobi': 15.6}

min_temp = float(input("Minimum temp: "))
print("Take a holiday to...")

for city, temp in temperatures.items():
    if temp >= min_temp:
        print(city)