"""
Problem Statement:
The road transport corporation (RTC) of a city wants to know whether a particular bus-route 
is running on profit or loss.

Assume that the following information are given:
- Price per litre of fuel = 70 Rs
- Mileage of the bus = 10 km/litre
- Price per ticket = 80 Rs

The bus runs on multiple routes having different distances (in kms) and number of passengers.
Write a function to calculate and return the profit earned (Rs) in each route.
Return -1 in case of loss.

#lex_auth_012693816779112448160
"""

def calculate(distance, no_of_passengers):
    """
    Calculates and returns the profit or loss for a bus route.

    Args:
        distance (float): Total distance of the route in kilometers.
        no_of_passengers (int): Total number of passengers.

    Returns:
        float: Profit amount if profitable, otherwise -1 for loss.
    """
    # Given constants
    PRICE_PER_LITRE = 70
    MILEAGE = 10
    TICKET_PRICE = 80

    # Calculate fuel cost for the route
    fuel_required = distance / MILEAGE
    fuel_cost = fuel_required * PRICE_PER_LITRE

    # Calculate total income from tickets
    total_income = no_of_passengers * TICKET_PRICE

    # Calculate profit or loss
    if total_income > fuel_cost:
        profit = total_income - fuel_cost
        return profit
    else:
        return -1


# Example test cases
print(calculate(20, 50))   # Expected: Profit (e.g., 50*80 - (20/10)*70 = 4000 - 140 = 3860)
print(calculate(100, 5))   # Expected: -1 (loss)
print(calculate(120, 150)) # Expected: Profit
