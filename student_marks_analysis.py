"""
Problem Statement:
A teacher is in the process of generating few reports based on the marks scored by the students 
of her class in a project-based assessment. Assume that the marks of her 10 students 
are available in a tuple. The marks are out of 25.

Write a Python program to implement the following functions:

1. find_more_than_average():
   - Find and return the percentage of students who have scored more than the average mark of the class.

2. generate_frequency():
   - Find how many students have scored the same marks.
   - For example, how many have scored 0, how many have scored 1, ..., how many have scored 25.
   - The result should be a list of 26 elements (0 to 25).

3. sort_marks():
   - Sort the marks in increasing order from 0 to 25 and return the sorted list.

Sample Input:
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)

Expected Output:
70.0
[0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
[2, 5, 12, 18, 18, 20, 20, 21, 24, 25]

#lex_auth_01269438947391897654
"""

# Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    """
    Returns the percentage of students who scored more than the class average.
    """
    average = sum(list_of_marks) / len(list_of_marks)
    count = 0
    for mark in list_of_marks:
        if mark > average:
            count += 1
    percentage = (count / len(list_of_marks)) * 100
    return percentage


def generate_frequency():
    """
    Returns a list showing how many students scored each mark from 0 to 25.
    """
    frequency = [0] * 26  # 0 to 25 marks
    for mark in list_of_marks:
        frequency[mark] += 1
    return frequency


def sort_marks():
    """
    Returns the marks sorted in ascending order.
    """
    return sorted(list_of_marks)


# Example outputs
print(find_more_than_average())  # Expected: 70.0
print(generate_frequency())      # Expected: [0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,2,0,2,1,0,0,1,1]
print(sort_marks())              # Expected: [2,5,12,18,18,20,20,21,24,25]
