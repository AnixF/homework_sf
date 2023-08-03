def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid

    return low


def sort_list(arr):
    return sorted(arr)


sequence = input("Введите последовательность чисел через пробел: ")
target_number = int(input("Введите любое число: "))

# Преобразуем введенную последовательность в список чисел
numbers = list(map(int, sequence.split()))

# Сортируем список по возрастанию
sorted_numbers = sort_list(numbers)

# Ищем позицию элемента, удовлетворяющего условию
position = binary_search(sorted_numbers, target_number)

# Проверяем соответствие условию и выводим результат
if position >= len(sorted_numbers) or sorted_numbers[position] != target_number:
    print("Указанное число не найдено или не соответствует условию.")
else:
    print(f"Номер позиции элемента: {position}")