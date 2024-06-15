def sum_of_squares(arr):
    return sum(x ** 2 for x in arr)

def filter_and_sum(arr):
    average = sum(arr) / len(arr)
    return sum(x for x in arr if x >= average)

from collections import Counter

def sort_by_frequency(arr):
    count = Counter(arr)
    return sorted(arr, key=lambda x: (-count[x], x))

def find_missing_number(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

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

def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

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

def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

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

import heapq


def k_closest_points(points, k):
    return heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)

    print(sum_of_squares([1, 2, 3]))
    print(filter_and_sum([1, 2, 3, 4, 10]))
    print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6]))
    print(find_missing_number([1, 2, 4, 5]))
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))
    print(rotate_array([1, 2, 3, 4, 5], 2))
    print(array_of_products([1, 2, 3, 4]))
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2))