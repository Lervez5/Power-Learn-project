# creates an empty list
my_list = []

# Step 2: Appends elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# step 3:inserts 15 at the second position
my_list.insert(1, 15)

# Step 4: Extend the list with [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort the list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_30 = my_list.index(30)
print("Index of 30:", index_30)

# Print final list to see changes
print("Final List:", my_list)