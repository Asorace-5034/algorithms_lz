import random as rd #импортируем все библиотеки
import math

nums_1 = rd.sample(range(1, 100000), k=100) #создаем список 1 без повторений
quantity_1 = 0 # количество операций
quantity_2 = 0


nums_2 = nums_1.copy() # Создаем копию массива 1


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
    return nums
        
        
# сортировка методом пузырька в убывание

def choose_buble (nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                global quantity_2
                quantity_2 += 1
                print(nums)
    return nums

choose_sort(nums_1) #вызываем функцию для сортировки выборкой и печататем готовый список
print(f"Количество операций методом выборки: {quantity_1}")
choose_buble(nums_2) # вызываем функцию для сортировки пузырьком и печатаем список
print(f"Количество операций методом пузырька: {quantity_2}")

