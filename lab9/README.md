# ����������� ������ �9: ��������� ������

## ���� ������

������� ������� ������ � ����������� �������� ��� ������ �� ����� ��������� ����� � ������ �� ����� ������ ������ �� ����.

## ���� ��������

� ��� ������������ ����� ������� �������� ��������� ������, �� ���������� ����� ��������� ��������.

1. ����� ������ ����� ��� ����� �� �����.
2. ����� ������ ��������� ���� ������ �����.
3. ����� ������ ����� IPv4 ������.
4. ����� ������ ������ ��� � ������ "HH:MM:SS".
5. ����� ������ ������ �������� ������ ���.
6. ����� ������ ����� ��'� �����������.
7. ����� ������ ������ ����� �������� ������.
8. ����� ������ ������ ���������� ����� � ������ ###-##-####.
9. ����� ������ ������ ������ (��������� ���� ������ �����, ���� ���� �����, ���� �����, ���� ����������� ������.
10. ����� ������ ����� IPv6 ������.

## ��������� ������

### ��������� �������:

main.py

README.md


### ���� ������� ����� �� ���� �����������

main.py: ������ ������� ��� �������� ����� �� ��������� ���������� ������.

### ���� �������� ������� �� ������ � ���������� �� ������

```python
import re

def task1(string):
  return bool(re.match(r'^[a-z0-9]+$', string))

def task2(string):
  return bool(re.search(r'[A-Z]', string))

def task3(string):
  return bool(re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', string))

def task4(string):
  return bool(re.match(r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$', string))

def task5(string):
  return bool(re.match(r'^\d{5}(-\d{4})?$', string))

def task6(string):
  return bool(re.match(r'^[a-z0-9_-]{6,12}$', string))

def task7(string):
  return bool(re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$', string))

def task8(string):
  return bool(re.match(r'^\d{3}-\d{2}-\d{4}$', string))

def task9(string):
  return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', string))

def task10(string):
  return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', string)) 
 ```
### �������� ������������

```
print(task1("hello123"))           # True
print(task2("Hello"))              # True
print(task3("192.168.1.1"))        # True
print(task4("12:34:56"))           # True
print(task5("12345"))              # True
print(task6("john_doe-123"))       # True
print(task7("4512-3456-7890-1234"))# True
print(task8("123-45-6789"))        # True
print(task9("Passw0rd#"))          # True
print(task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334")) # True
```

## ����������

```
task1("hello123") ������� True
```
```
task2("Hello") ������� True
```
```
task3("192.168.1.1") ������� True
```
```
task4("12:34:56") ������� True
```
```
task5("12345") ������� True
```
```
task6("john_doe-123") ������� True
```
```
task7("4512-3456-7890-1234") ������� True
```
```
task8("123-45-6789") ������� True
```
```
task9("Passw0rd#") ������� True
```
```
task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334") ������� True
```

## ��������

���� ������ ���� ���������. �� ��������� ������ �������� �������� �� ��������. ������� �� �������.

## ���������� � �������

��� ������� �������� ��������� ���� Python. ����� Python ������� ���� �� ����� 3.6. ��������� ��������: re.