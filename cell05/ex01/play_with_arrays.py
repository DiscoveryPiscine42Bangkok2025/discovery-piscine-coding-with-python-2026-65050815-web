#!/usr/bin/env python3
user_input = input("Please enter numbers separated by spaces: ")
original_array = list(map(int, user_input.split()))

new_array = []

for number in original_array:
    new_array.append(number + 2)

print(f"Original array: {original_array}")
print(f"New array: {new_array}")
