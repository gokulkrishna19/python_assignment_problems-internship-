# Program: Generate next 15 leap years
# Author: Gokul Krishna
# Description:
# Finds and displays the next 15 leap years starting from a given year.

def find_leap_years(given_year):
    list_of_leap_years = []

    for year in range(given_year, given_year + 100):  # Range large enough to cover 15 leap years
        # Leap year condition
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            list_of_leap_years.append(year)
        
        # Stop when 15 leap years are found
        if len(list_of_leap_years) == 15:
            break

    return list_of_leap_years


# Test case
list_of_leap_years = find_leap_years(2000)
print(list_of_leap_years)
