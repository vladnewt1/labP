import re
import math
from collections import defaultdict
from itertools import groupby

def interpolate_missing(arr):
    if not arr:
        return []

    n = len(arr)
    result = arr[:]

    for i in range(n):
        if result[i] is None:
            left = right = i
            while left >= 0 and result[left] is None:
                left -= 1
            while right < n and result[right] is None:
                right += 1

            if left >= 0 and right < n:
                result[i] = (result[left] + result[right]) / 2
            elif left >= 0:
                result[i] = result[left]
            elif right < n:
                result[i] = result[right]

    return result

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def process_batches(arr, batch_size):
    return [max(arr[i:i + batch_size]) for i in range(0, len(arr), batch_size)]

def encode_string(s):
    if not s:
        return ""

    encoded = []
    count = 1
    current_char = s[0]

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            encoded.append(f"{count if count > 1 else ''}{current_char}")
            current_char = char
            count = 1

    encoded.append(f"{count if count > 1 else ''}{current_char}")
    return ''.join(encoded)

def decode_string(encoded):
    decoded = []
    count = 0

    for char in encoded:
        if char.isdigit():
            count = count * 10 + int(char)
        else:
            decoded.append(char * (count if count else 1))
            count = 0

    return ''.join(decoded)

def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def regex_search(strings, pattern):
    regex = re.compile(pattern)
    return [s for s in strings if regex.search(s)]

def merge_sorted_arrays(arr1, arr2):
    return sorted(arr1 + arr2)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def group_by_key(data, key):
    grouped = defaultdict(list)
    for item in data:
        grouped[item[key]].append(item['value'])
    return dict(grouped)

def remove_outliers(data):
    if len(data) < 3:
        return data

    mean = sum(data) / len(data)
    std_dev = math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))
    lower_bound = mean - 2 * std_dev
    upper_bound = mean + 2 * std_dev

    return [x for x in data if lower_bound <= x <= upper_bound]

print(interpolate_missing([1, None, None, 4]))

for num in fibonacci(5):
    print(num)

print(process_batches([1, 2, 3, 4, 5, 6], 2))

encoded = encode_string("aaabbc")
print(encoded)
print(decode_string(encoded))

matrix = [
    [1, 2],
    [3, 4]
]
print(rotate_matrix(matrix)) 

print(regex_search(["test", "test123", "none"], "test\\d+"))

print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))

print(is_prime(11))

data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}]
print(group_by_key(data, 'key'))

print(remove_outliers([10, 100, 200, 300, 400, 500, 600]))