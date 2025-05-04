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
import random

numbers = [random.randint(1, 100) for _ in range(1000)]

count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

max_num = max(count_dict, key=count_dict.get)
max_count = count_dict[max_num]

print(f"Найчастіше повторюється число {max_num}, кількість повторів: {max_count}")

