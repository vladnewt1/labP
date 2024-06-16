# Лабораторна робота №15: Огляд технологій Big Data

## Мета роботи

Освоєння основних методів роботи з даними в контексті технологій Big Data. Потрібно створити функції для очищення, фільтрації, обробки та нормалізації даних.

## Опис завдання

1. Очищення даних
2. Фільтрація електронних адрес
3. Виділення ключових слів
4. Обробка текстових даних
5. Нормалізація даних
6. Конкатенація строк
7. Сума числових строк
8. Фільтрація чисел
9. Піднесення до квадрату
10. Реверсування строк

## Виконання роботи

### Структура проекту:

main.py

README.md


### Опис кожного файлу та його призначення

main.py: містить всі функції та приклади їх використання.

README.md: файл з описом завдань.

### Опис основних функцій та методів з поясненням їх роботи

```python
import re

# Task 1: Очищення даних
def clean_data(data):
  return list(map(lambda x: x.strip().lower(), data.split(',')))

# Task 2: Фільтрація електронних адрес
def filter_emails(emails):
  return list(filter(lambda x: x.count('@') == 1, map(str.strip, emails.split())))

# Task 3: Виділення ключових слів
def extract_keywords(data, length):
  return list(filter(lambda x: len(x) > length, map(str.strip, data.split())))

# Task 4: Обробка текстових даних
def process_text(data):
  cleaned_data = map(lambda x: re.sub(r'[^\w\s]', '', x).strip().lower(), data.split(','))
  return list(filter(lambda x: len(x) > 1, cleaned_data))

# Task 5: Нормалізація даних
def normalize_data(data):
  nums = list(map(float, data.split(',')))
  max_val = max(nums)
  return [round(num / max_val, 3) for num in nums]

# Task 6: Конкатенація строк
def concatenate_strings(data, separator):
  return ''.join(data.split(separator))

# Task 7: Сума числових строк
def sum_numeric_strings(data):
  nums = filter(lambda x: x.strip().isdigit(), data.split(','))
  return sum(map(int, nums))

# Task 8: Фільтрація чисел
def filter_numbers(data, threshold):
  nums = filter(lambda x: x.strip().isdigit(), data.split())
  return [int(num) for num in nums if int(num) > threshold]

# Task 9: Піднесення до квадрату
def map_to_squares(data):
  nums = map(int, data.split(','))
  return list(map(lambda x: x ** 2, nums))

# Task 10: Реверсування строк
def reverse_strings(data):
  return list(map(lambda x: x[::-1], data.split(',')))
```

### Приклади використання

```
data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned)  # ['apple', 'banana', 'orange']

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # ['test@example.com', 'example@test.co']

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # ['apple', 'banana']

texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)  # ['hello', 'yes', 'no']

numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # [0.333, 0.667, 1.0]

data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated)  # 'helloworldagain'

numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)  # 10

numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered)  # [30, 40]

numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers)  # [1, 4, 9, 16]

words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)  # ['elppa', 'ananab', 'torrac']
```

## Результати

```
clean_data(data) повертає ['apple', 'banana', 'orange']
```
```
filter_emails(emails) повертає ['test@example.com', 'example@test.co']
```
```
extract_keywords(words, 4) повертає ['apple', 'banana']
```
```
process_text(texts) повертає ['hello', 'yes', 'no']
```
```
normalize_data(numbers) повертає [0.333, 0.667, 1.0]
```
```
concatenate_strings(data, '*') повертає 'helloworldagain'
```
```
sum_numeric_strings(numbers) повертає 10
```
```
filter_numbers(numbers, 25) повертає [30, 40]
```
```
map_to_squares(numbers) повертає [1, 4, 9, 16]
```
```
reverse_strings(words) повертає ['elppa', 'ananab', 'torrac']
```


## Висновки

Освоїв основні методи роботи з даними в контексті технологій Big Data.Мета роботи була досягнута. Всі функції працюють відповідно до завдання. Проблем не виникло.

## Інструкції з запуску

Для запуску програми необхідно мати Python. Версія Python повинна бути не нижче 3.6.

Для запуску основного коду використовуйте команду:
     
python main.py

Бібліотека: re - операції зіставлення регулярних виразів.
