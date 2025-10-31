# Problem Statement:
# Write a python function, check_double(number) which accepts a whole number 
# and returns True if it satisfies the given conditions:
#
#   1. The number and its double should have exactly the same number of digits.
#   2. Both numbers should have the same digits, but in different order.
#
# Otherwise, it should return False.
#
# Example:
# If the number is 125874, its double is 251748 — both contain the same digits 
# but in a different order. Hence, the function should return True.
#
# Sample Input/Output:
# Input: 125874
# Output: True
#
# Input: 123456
# Output: False

def check_double(number):
    double_number = number * 2

    # Check if both numbers have same number of digits
    if len(str(number)) != len(str(double_number)):
        return False

    # Check if sorted digits match (same digits, different order)
    if sorted(str(number)) == sorted(str(double_number)):
        return True
    else:
        return False

# Test Cases
print(check_double(125874))   # Expected Output: True
print(check_double(123456))   # Expected Output: False
print(check_double(142857))   # Expected Output: True
