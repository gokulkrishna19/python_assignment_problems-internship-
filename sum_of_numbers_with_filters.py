"""
Problem Statement:
Consider sample data as follows: sample_data = range(1, 11)

Create two functions: odd() and even()
- The function even() returns a list of all the even numbers from sample_data.
- The function odd() returns a list of all the odd numbers from sample_data.

Create a function sum_of_numbers() which will accept the sample data and/or a function.
- If a function is not passed, sum_of_numbers() should return the sum of all the numbers from sample_data.
- If a function is passed, sum_of_numbers() should return the sum of numbers returned from the function passed.

#lex_auth_0127382164803993601239
"""

def sum_of_numbers(list_of_num, filter_func=None):
    """
    Returns the sum of numbers from list_of_num.
    If filter_func is provided, applies it to filter the numbers before summing.
    """
    if filter_func:
        filtered_list = filter_func(list_of_num)
        return sum(filtered_list)
    else:
        return sum(list_of_num)


def even(data):
    """
    Returns a list of even numbers from the given data.
    """
    even_list = []
    for i in data:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def odd(data):
    """
    Returns a list of odd numbers from the given data.
    """
    odd_list = []
    for i in data:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list


# Sample Data
sample_data = range(1, 11)

# Example Outputs
print("Sum of all numbers:", sum_of_numbers(sample_data))
print("Sum of even numbers:", sum_of_numbers(sample_data, even))
print("Sum of odd numbers:", sum_of_numbers(sample_data, odd))
