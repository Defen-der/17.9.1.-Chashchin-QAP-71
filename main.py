entered_numbers = input("Введите числа через пробел: ").split()
numbers = [int(i) for i in entered_numbers]
print("Вы ввели следующие числа:", numbers)

while True:
    try:
        element = int(input("Введите целое положительное число от 1 до 99: "))
        if element < 0 or element > 99:
            raise Exception
        break
    except ValueError:
        print("Введите число цифрами")
    except Exception:
        print("Введенное число выходит за пределы заданного диапазона")

numbers.append(element)

count = 0
for i in range(1, len(numbers)):
    x = numbers[i]
    idx = i
    while idx > 0 and numbers[idx-1] > x:
        numbers[idx] = numbers[idx-1]
        idx -= 1
        count += 1
    numbers[idx] = x

def binary_search(numbers, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if element == numbers[middle + 1]:
        return middle
    elif element < numbers[middle + 1]:
        return binary_search(numbers, element, left, middle - 1)
    else:
        return binary_search(numbers, element, middle + 1, right)


b_search = binary_search(numbers, element, 0, len(numbers))

print("Список после сортировки и дополнения: ", numbers)
print("Счетчик итераций при сортировке элементов списка: ", count)
print("Номер позиции добавленного в список элемента: ID = ", a)

if b_search > 0:
    print("Ответ: номер позиции элемента, который меньше введенного пользователем числа: ID = ",
          binary_search(numbers, element, 0, len(numbers)))
else:
    print("Перед введенным числом элементы в списке отсутствуют!")