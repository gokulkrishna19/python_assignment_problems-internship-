# Problem Statement:
# The Road Transport Corporation (RTC) of a city wants to know whether a particular bus route 
# is running on profit or loss.
#
# Given information:
#   - Price per litre of fuel = Rs.70
#   - Mileage of the bus = 10 km/litre
#   - Price per ticket = Rs.80
#
# The bus runs on multiple routes having different distances (in km) and number of passengers.
#
# Write a function to calculate and return the profit earned (in Rs) on each route.
# Return -1 in case of a loss.
#
# Sample Input/Output:
# Input:  distance = 20, no_of_passengers = 50
# Output: 3300
#
# Explanation:
#   Fuel needed = 20 / 10 = 2 litres
#   Cost of fuel = 2 * 70 = 140
#   Total ticket revenue = 50 * 80 = 4000
#   Profit = 4000 - 140 = 3860

def calculate(distance, no_of_passengers):
    # Constants
    fuel_price_per_litre = 70
    mileage = 10
    ticket_price = 80

    # Calculate total fuel cost and total ticket income
    fuel_needed = distance / mileage
    fuel_cost = fuel_needed * fuel_price_per_litre
    ticket_income = no_of_passengers * ticket_price

    # Determine profit or loss
    profit = ticket_income - fuel_cost

    if profit > 0:
        return int(profit)
    else:
        return -1

# Test Cases
distance = 20
no_of_passengers = 50
print(calculate(distance, no_of_passengers))  # Expected Output: 3860

distance = 100
no_of_passengers = 5
print(calculate(distance, no_of_passengers))  # Expected Output: -1
