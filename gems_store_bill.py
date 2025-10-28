# Program: ARS Gems Store Billing
# Author: Gokul Krishna
# Description:
# Calculates the bill amount for a list of gems and their required quantities.
# - If total bill > 30000, applies 5% discount.
# - If any gem is not available, returns -1.

def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    bill_amount = 0

    for i in range(len(reqd_gems)):
        if reqd_gems[i] in gems_list:
            index = gems_list.index(reqd_gems[i])
            bill_amount += price_list[index] * reqd_quantity[i]
        else:
            # Gem not available
            bill_amount = -1
            break

    # Apply 5% discount if applicable
    if bill_amount > 30000:
        bill_amount = bill_amount - (bill_amount * 0.05)

    return bill_amount


# List of gems available in the store
gems_list = ["Emerald", "Ivory", "Jasper", "Ruby", "Garnet"]

# Price of each gem (corresponds to gems_list)
price_list = [1760, 2119, 1599, 3920, 3999]

# Customer requirements
reqd_gems = ["Ivory", "Emerald", "Garnet"]
reqd_quantity = [3, 10, 12]

# Calculate and display bill amount
bill_amount = calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
