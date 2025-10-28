# Program: Find correctness of spellings
# Author: Gokul Krishna
# Description:
# Determines whether the contestant's spelling is CORRECT, ALMOST CORRECT, or WRONG.
# CORRECT  -> exact match
# ALMOST CORRECT -> at most 2 letters differ
# WRONG -> more than 2 differences or length mismatch

def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0

    for correct_word, given_word in word_dict.items():
        # Case 1: Check if length mismatch
        if len(correct_word) != len(given_word) or len(given_word) > 10:
            wrong += 1
            continue

        # Count letter mismatches
        mismatch = sum(1 for i in range(len(correct_word)) if correct_word[i] != given_word[i])

        if mismatch == 0:
            correct += 1
        elif mismatch <= 2:
            almost_correct += 1
        else:
            wrong += 1

    return [correct, almost_correct, wrong]


# Test case
word_dict = {
    "THEIR": "THEIR",
    "BUSINESS": "BISINESS",
    "WINDOWS": "WINDMILL",
    "WERE": "WEAR",
    "SAMPLE": "SAMPLE"
}

print(find_correct(word_dict))  # Expected Output: [2, 2, 1]
