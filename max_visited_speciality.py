# Program: Find the most visited medical speciality
# Author: Gokul Krishna
# Description:
# Finds the medical speciality with the maximum number of patient visits.
# Uses a predefined mapping between speciality codes and names.

def max_visited_speciality(patient_medical_speciality_list, medical_speciality):
    speciality_count = {}

    # Loop through the list (step by 2 since [ID, Code, ID, Code, ...])
    for i in range(1, len(patient_medical_speciality_list), 2):
        code = patient_medical_speciality_list[i]
        speciality_count[code] = speciality_count.get(code, 0) + 1

    # Find the speciality code with the maximum count
    max_code = max(speciality_count, key=speciality_count.get)

    # Return the full name from the dictionary
    return medical_speciality[max_code]


# Dictionary of specialities
medical_speciality = {
    "P": "Pediatrics",
    "O": "Orthopedics",
    "E": "ENT"
}

# Test cases
patient_list1 = [101, 'P', 102, 'O', 302, 'P', 305, 'P']
print(max_visited_speciality(patient_list1, medical_speciality))  # Pediatrics

patient_list2 = [101, 'O', 102, 'O', 302, 'P', 305, 'E', 401, 'O', 656, 'O']
print(max_visited_speciality(patient_list2, medical_speciality))  # Orthopedics

patient_list3 = [101, 'O', 102, 'E', 302, 'P', 305, 'P', 401, 'E', 656, 'O', 987, 'E']
print(max_visited_speciality(patient_list3, medical_speciality))  # ENT
