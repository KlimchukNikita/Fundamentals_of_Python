# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list_of_seasons = ['Winter', 'Spring', 'Summer', 'Autumn']

dict_of_seasons = {1 : 'Winter', 2 : 'Spring', 3 : 'Summer', 4 : 'Autumn'}

month = int(input("Enter the month number..."))

if month == 1 or month == 2 or month == 12:
    print(dict_of_seasons.get(1))
    print(list_of_seasons[0])

elif month == 3 or month == 4 or month == 5:
    print(dict_of_seasons.get(2))
    print(list_of_seasons[1])

elif month == 6 or month == 7 or month == 8:
    print(dict_of_seasons.get(3))
    print(list_of_seasons[2])

elif month == 9 or month == 10 or month == 11:
    print(dict_of_seasons.get(4))
    print(list_of_seasons[3])

else:
    print("There is no such month!")
