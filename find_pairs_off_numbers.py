"""
Problem Statement:
Write a python function, find_pairs_of_numbers() which accepts a list of positive integers 
with no repetitions and returns count of pairs of numbers in the list that adds up to n. 
The function should return 0, if no such pairs are found in the list.

Sample Input and Expected Output:

Input: [1, 2, 7, 4, 5, 6, 0, 3], 6
Output: 3

Input: [3, 4, 1, 8, 5, 9, 0, 6], 9
Output: 4
"""

def find_pairs_of_numbers(num_list, n):
    count = 0
    # Convert list to set to avoid duplicates
    setList = set(num_list)
    listSet = list(setList)
    
    # Compare all unique pairs
    for i in range(len(listSet)):
        for j in range(i + 1, len(listSet)):
            if listSet[i] + listSet[j] == n:
                count += 1
                
    return count


# Example test cases
if __name__ == "__main__":
    num_list1 = [1, 2, 7, 4, 5, 6, 0, 3]
    n1 = 6
    print(find_pairs_of_numbers(num_list1, n1))  # Expected output: 3

    num_list2 = [3, 4, 1, 8, 5, 9, 0, 6]
    n2 = 9
    print(find_pairs_of_numbers(num_list2, n2))  # Expected output: 4

    num_list3 = [1, 2, 4, 5, 6]
    n3 = 6
    print(find_pairs_of_numbers(num_list3, n3))  # Example case
