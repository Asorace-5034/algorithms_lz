import random as rd #импортируем все библиотеки

nums_1 = rd.sample(range(1, 100000), k=100) #создаем список 1
quantity_1 = 0 # количество сравнений
quantity_2 = 0


nums_2 = nums_1.copy() # Создаем копию массива 1
print(nums_1) #Выводим исходный массив
element = int(input('Введите число, которое вы хотите найти')) # Спрашиваем нужный элемент для поиска



# Цикл линейного поиска элемента
for i in range(len(nums_1)):
    if nums_1[i] == element:
        print(f"Индекс элемента: {i}")
        break
    else:
        quantity_1 += 1
        if quantity_1 == len(nums_1):
            print('Элемент не найден')
print(f'Количество сравнений по линейному поиску: {quantity_1}') # выводим



first = 0 #для сравнения переменная
last = len(nums_2) - 1 # Последний индекс
index = -1 #Просто индекс

#цикл сравнения методом бинарного поиска
while (first <= last) and (index == -1):
    mid = (first+last)//2
    if nums_2[mid] == element:
        print(f"Индекс элемента: {mid}")
        break
    else:
        quantity_2 += 1
        if quantity_2 == len(nums_2):
            print('Элемент не найден')
        elif element<nums_2[mid]:
            last = mid -1
        else:
            first = mid +1
print(f'Количество сравнений по линейному поиску: {quantity_2}') # выводим






