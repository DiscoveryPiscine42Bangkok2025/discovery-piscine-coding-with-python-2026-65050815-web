#!/usr/bin/env python3
user_input = input("Please enter numbers separated by spaces: ")
original_array = list(map(int, user_input.split()))

new_array = []

for number in original_array:
    if number > 5:
        new_array.append(number + 2)

new_array = list(set(new_array))

print(original_array)
print(new_array)
