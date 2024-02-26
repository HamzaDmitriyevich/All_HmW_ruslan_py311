def calculate_vacation_days_and_pay(start_date):
    # Первоначальные данные
    salary = 0
    vacation_days = 0
    vacation_pay = 0

    # Разбиваем дату начала работы на год, месяц и день
    start_year, start_month, start_day = map(int, start_date.split('-'))

    # Определяем количество полных месяцев с момента начала работы
    months_worked = (2024 - start_year) * 12 + (2 - start_month)  # Предполагаем, что сейчас февраль 2024 года

    # Рассчитываем зарплату и количество дней отпуска на конец каждого месяца
    for month in range(1, months_worked + 1):
        salary += 100
        vacation_days += 2 if month % 2 == 0 else 0
        vacation_pay = salary

    return vacation_days, vacation_pay

# Ввод даты начала работы
start_date = input("Введите дату начала работы (гггг-мм-дд): ")

vacation_days, vacation_pay = calculate_vacation_days_and_pay(start_date)
print(f"Количество дней отпуска: {vacation_days}")
print(f"Сумма отпускных: {vacation_pay} рублей")
