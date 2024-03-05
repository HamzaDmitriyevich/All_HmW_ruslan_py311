def put_v_library():
    question = input('How to get to the library')
    return question


vyzov = put_v_library()
rasdel = vyzov.split()[0]
print(rasdel)



#1. Спросить человека маршрут ("как пройти в библиотеку"). Получить ответ в виде строки. Сохранить в переменную. Вывести первое слово ответа на экран