# Лабораторна робота №10: Об'єктно-орієнтоване програмування в Python

## Мета роботи

Освоєння навичок роботи з об'єктно-орієнтованим програмуванням в Python. Потрібно створити класи, використовувати методи, наслідування.

## Опис завдання

1. Створення класу `Student`.
2. Додавання методу до класу `Student`.
3. Наслідування класів `Animal` та `Dog`.
4. Поліморфізм з класами `Bird`, `Sparrow` та `Penguin`.
5. Інкапсуляція в класі `Encapsulation`.
6. Створення класу `Rectangle` для обчислення периметра.
7. Створення класу `AverageCalculator` для обчислення середнього арифметичного.

## Виконання роботи

### Структура проекту:

main.py

README.md


### Опис кожного файлу та його призначення

main.py: містить всі класи та приклади їх використання.

### Опис основних функцій та методів з поясненням їх роботи

```python
# Task 1: Class Creation
class Student:
  def __init__(self, name, age, grade):
      self.name = name
      self.age = age
      self.grade = grade

# Task 2: Create Method
class Student:
  def __init__(self, name, age, grade):
      self.name = name
      self.age = age
      self.grade = grade

  def display_info(self):
      return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Task 3: Inheritance
class Animal:
  def __init__(self, name, sound):
      self.name = name
      self.sound = sound

  def make_sound(self):
      return f"{self.name}: {self.sound}"

class Dog(Animal):
  def __init__(self, name, sound, breed):
      super().__init__(name, sound)
      self.breed = breed

# Task 4: Polymorphism
class Bird:
  def fly(self):
      return None

class Sparrow(Bird):
  def fly(self):
      return "Sparrow flies high"

class Penguin(Bird):
  def fly(self):
      return "Penguin cannot fly"

# Task 5: Encapsulation
class Encapsulation:
  def __init__(self, public, private, protected):
      self.public = public
      self._private = private
      self.__protected = protected

# Task 6: Rectangle
class Rectangle:
  def __init__(self, width, height):
      self.width = width
      self.height = height

  def calculate_perimeter(self):
      return 2 * (self.width + self.height)

# Task 7: AverageCalculator
class AverageCalculator:
  def __init__(self, numbers):
      self.numbers = numbers

  def calculate_average(self):
      return sum(self.numbers) / len(self.numbers)
```

### Приклади використання

```
# Task 1 and 2
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info())  # Name: Ivan, Age: 30, Grade: 2

# Task 3
animal = Animal(name="Lala", sound=" ")
dog = Dog(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound())  # Lala:  
print(dog.make_sound())  # Lala: Auuuuuuu

# Task 4
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly())  # None
print(sparrow.fly())  # Sparrow flies high
print(penguin.fly())  # Penguin cannot fly

# Task 5
obj = Encapsulation(1, 2, 3)
print(obj.public)  # 1
print(obj._private)  # 2
print(obj._Encapsulation__protected)  # 3

# Task 6
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter())  # 18

# Task 7
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average())  # 12.5
```

## Результати

```
student.display_info() повертає Name: Ivan, Age: 30, Grade: 2
```
```
animal.make_sound() повертає Lala:
```
```
dog.make_sound() повертає Lala: Auuuuuuu
```
```
bird.fly() повертає None
```
```
sparrow.fly() повертає Sparrow flies high
```
```
penguin.fly() повертає Penguin cannot fly
```
```
obj.public повертає 1
```
```
obj._private повертає 2
```
```
obj._Encapsulation__protected повертає 3
```
```
rectangle.calculate_perimeter() повертає 18
```
```
avg_calculator.calculate_average() повертає 12.5
```


## Висновки

Освоїв навички роботи з об'єктно-орієнтованим програмуванням в Python. Мета роботи була досягнута. Всі класи та методи працюють відповідно до завдання. Проблем не виникло.

## Інструкції з запуску

Для запуску програми необхідно мати Python. Версія Python повинна бути не нижче 3.6. 
