# Лабораторна робота №12: Використання вкладених списків для створення та маніпулювання двовимірними структурами даних

## Мета роботи

Освоєння навичок роботи з двовимірними структурами даних у Python шляхом створення класу Matrix з методами для додавання елементів, транспонування.

## Опис завдання

1. Створити клас Matrix, який ініціалізує двовимірний список нулями.
2. Додати метод add_element для додавання елементу.
3. Додати метод sum_of_rows, який повертає список сум кожного рядка.
4. Додати метод transpose, який повертає новий об'єкт Matrix.
5. Додати метод multiply_by, що є результатом множення двох матриць.
6. Додати метод is_symmetric, який перевіряє, чи є матриця симетричною.
7. Додати метод rotate_right, який повертає матрицю, повернуту на 90 градусів вправо.
8. Додати метод flatten, який повертає одномірний список, що містить всі елементи матриці.
9. Додати статичний метод from_list, який створює об'єкт матриці з заданого списку списків.
10. Додати метод diagonal, який витягує діагональ квадратної матриці як список.

## Виконання роботи

### Структура проекту:

main.py

README.md


### Опис кожного файлу та його призначення

main.py: містить клас Matrix з реалізованими методами та приклади їх використання.

### Опис основних функцій та методів з поясненням їх роботи

```python
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0] * cols for _ in range(rows)]

    def add_element(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            raise IndexError("Row or column index out of bounds.")

    def sum_of_rows(self):
        return [sum(row) for row in self.data]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        transposed_matrix = Matrix(self.cols, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions do not match for multiplication.")
        result_matrix = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                result_matrix.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
        return result_matrix

    def is_symmetric(self):
        if self.rows != self.cols:
            return False
        return self.data == self.transpose().data

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.cols)]
        self.data = rotated_data
        self.rows, self.cols = self.cols, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        cols = len(list_of_lists[0]) if rows > 0 else 0
        matrix = Matrix(rows, cols)
        matrix.data = list_of_lists
        return matrix

    def diagonal(self):
        if self.rows != self.cols:
            raise ValueError("Matrix is not square.")
        return [self.data[i][i] for i in range(self.rows)]
```

### Приклади використання

```
# Task 1: Створення матриці
matrix = Matrix(2, 3)
print(matrix.data)  # [[0, 0, 0], [0, 0, 0]]

# Task 2: Додавання елемента до матриці
matrix.add_element(1, 2, 10)
print(matrix.data)  # [[0, 0, 0], [0, 0, 10]]
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows())  # [15, 20]

# Task 3: Сума у рядках
print(matrix.sum_of_rows())  # [15, 20]

# Task 4: Транспонована матриця 
matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data)  # [[0, 0], [1, 0], [0, 2]]

# Task 5: Множення матриць
matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data)  # [[14, 0], [0, 0]]

# Task 6: Перевірка симетричності матриці
matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric())  # True

# Task 7: Обернена матриця
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data)  # [[3, 1], [4, 2]]

# Task 8: Перетворення матриці в масив
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten())  # [1, 2, 3, 4]

# Task 9: Створення матриці з списку
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data)  # [[1, 2], [3, 4]]

# Task 10: Отримання діагональної матриці
matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal())  # [1, 2, 3]
```

## Результати

```
matrix = Matrix(2, 3)
print(matrix.data)  # [[0, 0, 0], [0, 0, 0]]
```
```
matrix.add_element(1, 2, 10)
print(matrix.data)  # [[0, 0, 0], [0, 0, 10]]
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows())  # [15, 20]
```
```
print(matrix.sum_of_rows())  # [15, 20]```
```

## Висновки

Освоїв навички роботи з двовимірними структурами даних. Мета роботи була досягнута. Мета роботи була досягнута. Всі методи працюють відповідно до завдань. Проблем не виникло.

## Інструкції з запуску

Для запуску програми необхідно мати Python. Версія Python повинна бути 3.12. Запустити програму.

