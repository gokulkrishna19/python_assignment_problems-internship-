# Problem Statement:
# Consider sample data as follows: sample_data = range(1, 11)
#
# Create two functions: odd() and even()
#   - The function even() returns a list of all the even numbers from sample_data
#   - The function odd() returns a list of all the odd numbers from sample_data
#
# Create a function sum_of_numbers() which will accept the sample data and/or a function.
#   - If a function is not passed, the sum_of_numbers() should return the sum of all numbers from sample_data
#   - If a function is passed, the sum_of_numbers() should return the sum of numbers returned from the function passed.
#
# Sample Input/Output:
# sum_of_numbers(sample_data)              ➞ 55
# sum_of_numbers(sample_data, even)        ➞ 30
# sum_of_numbers(sample_data, odd)         ➞ 25

def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func is None:
        return sum(list_of_num)
    else:
        return sum(filter_func(list_of_num))

def even(data):
    even_list = []
    for num in data:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

def odd(data):
    odd_list = []
    for num in data:
        if num % 2 != 0:
            odd_list.append(num)
    return odd_list

# Sample Data
sample_data = range(1, 11)

# Test Cases
print(sum_of_numbers(sample_data))          # Expected Output: 55
print(sum_of_numbers(sample_data, even))    # Expected Output: 30
print(sum_of_numbers(sample_data, odd))     # Expected Output: 25
