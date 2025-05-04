Завдання 1 
cities = ["Київ", "Одеса", "Львів", "Харків", "Житомир"]
city_set = set(cities)  # Множина для швидкого пошуку

for city in ["Одеса", "Полтава"]:
    if city in city_set:
        print(f"Місто {city} є у списку.")
    else:
        print(f"Місто {city} відсутнє у списку.")

Завдання 2
students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть ім’я студента: ")

try:
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print("Студента з таким ім'ям не знайдено.")

Завдання 3
students = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть ім’я студента: ")

try:
    print(f"Оцінка студента {name}: {students[name]}")
except KeyError:
    print("Студента з таким ім'ям не знайдено.")
