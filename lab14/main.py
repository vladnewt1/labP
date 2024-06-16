def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(x, y):
    return x == y

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(condition):
    return "Hello, World!" if condition else "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y != z != x:
        return "All different"
    else:
        return "Neither"

def count_true(lst):
    return sum(lst)

def parity(num):
    return bin(num).count('1') % 2 == 0

def majority_vote(a, b, c):
    return sum([a, b, c]) > 1

def switch(value):
    return not value

def ternary_check(condition, true_result, false_result):
    return true_result if condition else false_result

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(lst):
    return [x for x in lst if x]

def multiplexer(a, b, c, n):
    if a:
        return n * 2
    elif b:
        return n * 3
    elif c:
        return n - 5
    else:
        return n

print(check_truth(True, False, True))
print(logical_equivalence(True, True))
print(logical_equivalence(True, False))
print(xor(True, False))
print(xor(True, True))
print(greet(True))
print(greet(False))
print(nested_condition(3, 3, 3))
print(nested_condition(3, 4, 5))
print(count_true([True, False, True, False, True]))
print(parity(3))
print(parity(4))
print(majority_vote(True, True, False))
print(majority_vote(False, False, True))
print(switch(True))
print(switch(False))
print(ternary_check(True, "Yes", "No"))
print(ternary_check(False, "Yes", "No"))
print(validate(True, False, True))
print(validate(False, True, True))
print(validate(False, False, True))
print(chain_check(1, 2, 3))
print(chain_check(3, 2, 1))
print(chain_check(1, 3, 2))
print(filter_true([True, False, True, False]))
print(multiplexer(False, False, True, 10))
print(multiplexer(True, False, False, 10))
print(multiplexer(False, True, False, 10))
print(multiplexer(False, False, False, 10))