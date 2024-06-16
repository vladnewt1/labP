import re
def clean_data(data):
    return list(map(lambda x: x.strip().lower(), data.split(',')))

def filter_emails(emails):
    return list(filter(lambda x: x.count('@') == 1, map(str.strip, emails.split())))

def extract_keywords(data, length):
    return list(filter(lambda x: len(x) > length, map(str.strip, data.split())))

def process_text(data):
    cleaned_data = map(lambda x: re.sub(r'[^\w\s]', '', x).strip().lower(), data.split(','))
    return list(filter(lambda x: len(x) > 1, cleaned_data))

def normalize_data(data):
    nums = list(map(float, data.split(',')))
    max_val = max(nums)
    return [round(num / max_val, 3) for num in nums]

def concatenate_strings(data, separator):
    return ''.join(data.split(separator))

def sum_numeric_strings(data):
    nums = filter(lambda x: x.strip().isdigit(), data.split(','))
    return sum(map(int, nums))

def filter_numbers(data, threshold):
    nums = filter(lambda x: x.strip().isdigit(), data.split())
    return [int(num) for num in nums if int(num) > threshold]

def map_to_squares(data):
    nums = map(int, data.split(','))
    return list(map(lambda x: x ** 2, nums))

def reverse_strings(data):
    return list(map(lambda x: x[::-1], data.split(',')))

data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned) 
emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)
words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)
texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)
numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)
data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated)
numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum)
numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered)
numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers)
words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words)