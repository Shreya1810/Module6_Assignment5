# Task 2: Demonstrate List Slicing
# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

original_list = [1,2,3,4,5,6,7,8,9,10]
print(f"Original list: {original_list}")
first_five = original_list[:5]
print(f"Extracted first five elements: {first_five}")
reverse_list = first_five[::-1]
print(f"Reversed extracted elements: {reverse_list}")

