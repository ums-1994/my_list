# Create an empty list
my_list = []

# Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position
my_list.insert(1, 15)

# Extend my_list with another list
my_list.extend([50, 60, 70])

# Remove the last element from my_list
my_list.pop()  # This removes 70, the last element

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print(f"The index of the value 30 in my_list is: {index_of_30}")

# Print the final state of the list
print("Final my_list:", my_list)