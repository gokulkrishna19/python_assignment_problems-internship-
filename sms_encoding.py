# Program: SMS Encoding
# Author: Gokul Krishna
# Description:
# Converts a sentence into an SMS-style abbreviated form.
# Retains only consonants from each word unless the word is made up only of vowels.
# Spaces are preserved as is.

def sms_encoding(data):
    vowels = 'aeiouAEIOU'
    result = []

    for word in data.split():
        # Retain only consonants from the word
        consonants = ''.join([ch for ch in word if ch not in vowels])

        # If the word has only vowels, keep it as is
        if consonants == '':
            result.append(word)
        else:
            result.append(consonants)

    # Join the processed words with spaces
    return ' '.join(result)


# Test cases
data1 = "I love Python"
print(sms_encoding(data1))  # Output: I lv Pythn

data2 = "MSD says I love cricket and tennis too"
print(sms_encoding(data2))  # Output: MSD sys I lv crckt nd tnns t

data3 = "I will not repeat mistakes"
print(sms_encoding(data3))  # Output: I wll nt rpt mstks
