import random                                         #Імпорт бібліотеки random                          
rows = int(input('Введіть ціле число рядків масиву'))            #Рядки масиву
columns = int(input('Введіть ціле число колонок масиву'))        #Колонки масиву
array = [[random.randint(1, 99) for _ in range(columns)] for _ in range(rows)]  #Створення списку
print("Початковий масив:") 
for row in array:
    for num in row:
        print(f"{num:< {rows+1}}", end=' ')
    print() #Виведення початкового масиву
sorted_array = sorted(array, key=lambda row: sum(row)) #Сортування масиву та параметр який вказує на функцію яка визначає критерій сортування
print("\nМасив після сортування за сумою:")
for row in sorted_array:
    for num in row:
        print(f"{num:<{rows+1}}", end=' ')
    print() #Відсортований масив