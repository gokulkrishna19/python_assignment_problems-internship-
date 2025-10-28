# Program: Find the word with the highest frequency in a text
# Author: Gokul Krishna
# Description: Displays the word with the largest frequency.
# In case of a tie, the longest word is selected.
# Case-insensitive comparison; only spaces are considered as separators.

def max_frequency_word_counter(data):
    # Convert to lowercase and remove commas
    data = data.replace(",", "").lower()
    words = data.split()

    # Create frequency dictionary
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1

    # Find the maximum frequency
    max_freq = max(freq.values())

    # Filter words with maximum frequency
    max_words = [word for word, count in freq.items() if count == max_freq]

    # Choose the longest word among them
    result_word = max(max_words, key=len)

    # Print result in required format
    print(result_word, max_freq)


# Test case 1
data = "Work like you do not need money, love like you have never been hurt, and dance like no one is watching"
max_frequency_word_counter(data)

# Test case 2
data = "Courage is not the absence of fear but rather the judgement that something else is more important than fear"
max_frequency_word_counter(data)
