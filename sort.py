import random as rd #импортируем все библиотеки
import math

nums_1 = [] #создаем список 1
quantity_1 = 0 # количество операций
quantity_2 = 0

for i in range(10):
    nums_1.append(rd.randint(1,100)) # создаем массив чисел по условию

nums_2 = nums_1.copy()


print('Исходное множество',nums_1)
print('Исходное множество',nums_2)

# сортировка методм выбора в убывание   
def choose_sort (nums):
    for i in range (len(nums)):
        print(nums)
        lowest_value_index = i
        for j in range (i + 1, len(nums)):
            if nums[j] > nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
        global quantity_1
        quantity_1 += 1
        
        
# сортировка методом пузырька в убывание

def choose_buble (nums):
    for i in range(len(nums_2)):
        print(nums)
        for j in range(len(nums_2) - 1 - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
            
        global quantity_2
        quantity_2 +=1

choose_sort(nums_1) #вызываем функцию для сортировки выборкой и печататем готовый список
print(f"Количество операций методом выборки: {quantity_1}")
choose_buble(nums_2) # вызываем функцию для сортировки пузырьком и печатаем список
print(f"Количество операций методом пузырька: {quantity_2}")

