"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды
и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""

time = int(input("Enter the time in seconds... "))

hours = time // 3600
minutes = time / 60
seconds = minutes / 60

print(f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}")
