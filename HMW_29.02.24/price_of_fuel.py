#На оптовую базу прибыл человек готовый купить топливо по определенной цене
#Цена не должна быть слишком низкой и быть <0 за бензин и < 0 за дизель
#нужно написать программу котораяч не позволит это сделать, цена не  должна быть очень высокой



try: 

    fuel_benzin = input("Введите цену на бензин") # Инпуты
    fuel_disel = input('Введите цену Дизеля')
    kol_benzina = input('Введите количество литров бензина')
    kol_disel = input('Введите количество литров Дизеля')
    
    litry_benz = int(kol_benzina) #Приводим стринг к инт
    litry_disel = int(kol_disel)
    benzin = int(fuel_benzin)
    disel = int(fuel_disel)
    

    
    if benzin <= 0 :
        raise ValueError ("Цена не можеть быть равна 0 или быть отрицательной!")

    
    if disel <= 0:
        raise ValueError ("Цена на дизель не может быть меньше или равняться нулю")

    if benzin > 100 :
        raise ValueError ("Оу дружок цена высоковата")

    if disel > 80 :
        raise ValueError ("Ты Шо?") 
    

    result1 =   disel * litry_disel #Результаты вычислений
    result2 = benzin * litry_benz


    print(f"Стоимость Дизеля: {result1}") # Интернет сказал что так выводить лучше
    print(f"Стоимость Бензина: {result2}")
    
except ValueError: 
    print("Не гони дурю паря, пиши адекватные цены")
  
    