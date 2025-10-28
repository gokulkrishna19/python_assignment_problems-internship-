# Program: Create the largest possible number
# Author: Gokul Krishna
# Description:
# Given a list of two-digit numbers, this program arranges them to form the largest possible number.

def create_largest_number(number_list):
    # Sort numbers in descending order
    sorted_list = sorted(number_list, reverse=True)
    
    # Concatenate them as strings
    new_string = ''.join(str(num) for num in sorted_list)
    
    # Convert to integer before returning
    largest_number = int(new_string)
    return largest_number


# Test case 1
number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)  # Expected Output: 674523

# Test case 2
number_list = [23, 34, 55]
largest_number = create_largest_number(number_list)
print(largest_number)  # Expected Output: 553423
