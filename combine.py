# Create the two lists
list_1 = [1, 2, 4]
list_2 = [1, 3, 5]

# Find elements that are in second but not in first
list_1.extend(list_2)
combined = list(set(list_1))

# Create the new list using list concatenation

print (combined)
# [1, 2, 3, 4, 5]