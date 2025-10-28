# Problem Statement:
# A teacher is conducting a camp for a group of five children. Based on their performance and behavior during the camp,
# the teacher rewards them with chocolates.
#
# Write a Python function to:
#
# 1. Find the total number of chocolates received by all the children put together.
#    Assume that each child is identified by an id and it is stored in a tuple and
#    the number of chocolates given to each child is stored in a list.
#
# 2. The teacher also rewards a child with few extra chocolates for his/her best conduct during the camp.
#    If the number of extra chocolates is less than 1, display "Extra chocolates is less than 1".
#    If the given child Id is invalid, display "Child id is invalid".
#    Otherwise, add the extra chocolates to the respective child and display the updated list.

#lex_auth_01269442027919769669

# Global variables
child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

def calculate_total_chocolates():
    # Remove pass and write your logic here to find and return the total number of chocolates
    total = sum(chocolates_received)
    return total

def reward_child(child_id_rewarded, extra_chocolates):
    # Remove pass and write your logic here
    if extra_chocolates < 1:
        print("Extra chocolates is less than 1")
        return
    if child_id_rewarded not in child_id:
        print("Child id is invalid")
        return
    index = child_id.index(child_id_rewarded)
    chocolates_received[index] += extra_chocolates
    print(chocolates_received)

# Display total chocolates
print(calculate_total_chocolates())

# Test your code by passing different values for child_id_rewarded, extra_chocolates
reward_child(20, 2)
