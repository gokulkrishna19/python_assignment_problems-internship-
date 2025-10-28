# Program: Check if a string is a palindrome
# Author: Gokul Krishna
# Description:
# This program checks whether a given string is a palindrome or not.
# It assumes that all letters are of the same case.

def check_palindrome(word):
    # Reverse the string
    reversed_word = word[::-1]
    
    # Compare original and reversed strings
    if reversed_word == word:
        return True
    else:
        return False


# Test cases
test_words = ["malayalam", "civic", "WOW", "python", "level"]

for word in test_words:
    if check_palindrome(word):
        print(f"'{word}' is a palindrome")
    else:
        print(f"'{word}' is not a palindrome")
