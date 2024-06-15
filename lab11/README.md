# Лабораторна робота №11: Розширена робота з масивами чисел в Python

## Мета роботи

Освоєння навичок роботи з масивами чисел, включаючи операції з масивами, сортування, обробку послідовностей.

## Опис завдання

1. Сума квадратів чисел у масиві.
2. Фільтрація чисел, що більші або дорівнюють середньому значенню масиву, та їх сума.
3. Сортування масиву за частотою зустрічань елементів.
4. Пошук відсутнього числа в масиві.
5. Пошук найдовшої послідовності з послідовних чисел.
6. Поворот масиву вправо на k позицій.
7. Обчислення масиву добутків всіх чисел, крім числа на поточному індексі.
8. Знаходження максимальної суми підмасиву.
9. Виведення елементів 2D матриці в спіральному порядку.
10. Знаходження k найближчих точок до початку координат у 2D площині.

## Виконання роботи

###  Структура проекту:

main.py

README.md


### Опис кожного файлу та його призначення

main.py: містить всі функції та приклади їх використання.

### Опис основних функцій та методів з поясненням їх роботи

```python
# Task 1: Сума квадратів
def sum_of_squares(arr):
  return sum(x ** 2 for x in arr)

# Task 2: Фільтрування та обчислення суми
def filter_and_sum(arr):
  average = sum(arr) / len(arr)
  return sum(x for x in arr if x >= average)

# Task 3: Сортування масиву
from collections import Counter

def sort_by_frequency(arr):
  count = Counter(arr)
  return sorted(arr, key=lambda x: (-count[x], x))

# Task 4: Знаходження відсутнього числа
def find_missing_number(arr):
  n = len(arr) + 1
  total_sum = n * (n + 1) // 2
  return total_sum - sum(arr)

# Task 5: Найдовша послідовна послідовність
def longest_consecutive(arr):
  num_set = set(arr)
  longest_streak = 0
  for num in arr:
      if num - 1 not in num_set:
          current_num = num
          current_streak = 1
          while current_num + 1 in num_set:
              current_num += 1
              current_streak += 1
          longest_streak = max(longest_streak, current_streak)
  return longest_streak

# Task 6: Повернути масив
def rotate_array(arr, k):
  k = k % len(arr)
  return arr[-k:] + arr[:-k]

# Task 7: Обчислення масиву добутків всіх чисел
def array_of_products(arr):
  n = len(arr)
  left_products = [1] * n
  right_products = [1] * n
  products = [1] * n
  for i in range(1, n):
      left_products[i] = left_products[i - 1] * arr[i - 1]
  for i in range(n - 2, -1, -1):
      right_products[i] = right_products[i + 1] * arr[i + 1]
  for i in range(n):
      products[i] = left_products[i] * right_products[i]
  return products

# Task 8: Знаходження максимальної суми підмасиву
def max_subarray_sum(arr):
  max_sum = current_sum = arr[0]
  for num in arr[1:]:
      current_sum = max(num, current_sum + num)
      max_sum = max(max_sum, current_sum)
  return max_sum

# Task 9: Виведення елементів 2D матриці в спіральному порядку
def spiral_order(matrix):
  result = []
  while matrix:
      result += matrix.pop(0)
      if matrix and matrix[0]:
          for row in matrix:
              result.append(row.pop())
      if matrix:
          result += matrix.pop()[::-1]
      if matrix and matrix[0]:
          for row in matrix[::-1]:
              result.append(row.pop(0))
  return result

# Task 10: Знаходження k найближчих точок до початку координат
import heapq

def k_closest_points(points, k):
  return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
```

### Приклади використання

```
# Task 1
print(sum_of_squares([1, 2, 3]))  # 14 

# Task 2
print(filter_and_sum([1, 2, 3, 4, 10]))  # 14 

# Task 3
print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))  # [4, 4, 4, 6, 6, 6, 2] 

# Task 4
print(find_missing_number([1, 2, 4, 5]))  # 3 

# Task 5
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 

# Task 6
print(rotate_array([1, 2, 3, 4, 5], 2))  # [4, 5, 1, 2, 3] 

# Task 7
print(array_of_products([1, 2, 3, 4]))  # [24, 12, 8, 6]

# Task 8
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 

# Task 9
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1, 2, 3, 6, 9, 8, 7, 4, 5] 

# Task 10
print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))  # [(1, 1), (1, 2)]
```

## Результати

```
sum_of_squares([1, 2, 3]) повертає 14
```
```
filter_and_sum([1, 2, 3, 4, 10]) повертає 14
```
```
sort_by_frequency([4, 6, 2, 6, 4, 4, 6]) повертає [4, 4, 4, 6, 6, 6, 2]
```
```
find_missing_number([1, 2, 4, 5]) повертає 3
```
```
longest_consecutive([100, 4, 200, 1, 3, 2]) повертає 4
```
```
rotate_array([1, 2, 3, 4, 5], 2) повертає [4, 5, 1, 2, 3]
```
```
array_of_products([1, 2, 3, 4]) повертає [24, 12, 8, 6]
```
```
max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) повертає 6
```
```
spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) повертає [1, 2, 3, 6, 9, 8, 7, 4, 5]
```
```
k_closest_points([(1, 2), (1, 1), (3, 4)], 2) повертає [(1, 1), (1, 2)]
```

## Висновки

Освоїв навички роботи з масивами. Мета роботи була досягнута. Всі функції працюють відповідно до завдання. Проблем не виникло.

## Інструкції з запуску

Для запуску програми необхідно мати Python. Версія Python повинна бути 3.12. Запустити програму.
Бібліотека: heapq.

