import calendar

# Запросить у пользователя ввод месяца и года
year = int(input("Введите год: "))
month = int(input("Введите месяц: "))

# Вывести календарь для указанного месяца и года
print(calendar.month(year, month))
