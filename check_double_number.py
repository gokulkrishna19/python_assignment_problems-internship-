"""
Problem Statement:
Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions:

1. The number and its double should have exactly the same number of digits.
2. Both the numbers should have the same digits, but in a different order.

Otherwise, it should return False.

Example:
If the number is 125874 and its double (251748) contain exactly the same digits, 
but in a different order, the function should return True.
"""

def check_double(number):
    double_number = number * 2  # Correct doubling
    str_num = str(number)
    str_double = str(double_number)

    # Check 1: Same number of digits
    if len(str_num) != len(str_double):
        return False

    # Check 2: Same digits, but not in the same order
    if sorted(str_num) == sorted(str_double) and str_num != str_double:
        return True
    else:
        return False


# Test cases
print(check_double(125874))  # ✅ True (digits match, order different)
print(check_double(125875))  # ❌ False (digits differ)
print(check_double(142857))  # ✅ True (famous cyclic number)
print(check_double(10))      # ❌ False (digits count differ)
