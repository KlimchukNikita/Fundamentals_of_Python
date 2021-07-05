# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time = int(input("Enter time in seconds..."))

hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + minutes * 60)

print(f"Time in format hh:mm:ss... {hours} : {minutes} : {seconds}")
