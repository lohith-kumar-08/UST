rohit_sl = [100, 264, 50, 45, 160, 89, 200]

# Print type 
print(type(rohit_sl))

# Add element at the end of the list
rohit_sl.append(0)

# Add element at a specific position 
rohit_sl.insert(2, 0)

# Add another list to the existing list
rohit_ipl = [100, 30, 40]
rohit_sl.extend(rohit_ipl)

# Update the existing item at index 5
rohit_sl[5] = 180

print(rohit_sl)

# Example of a tuple inside the list
user_details = [("parag", 40), ("prachi", 39), ("kailas", 34), ("pankaja", 24)]

# Loop through the user_details list and print the names and ages
for user in user_details:
    print(user[0], "has an age of", user[1], "years")

# Remove the last item from the list
rohit_sl.pop()

# Remove an item based on the value 
rohit_sl.remove(50)

print(rohit_sl)

# Sort the list in ascending order
rohit_sl.sort()

print("Sorted in ascending order:", rohit_sl)

# Reverse the list to make it descending
rohit_sl.reverse()

print("Sorted in descending order:", rohit_sl)

# Count occurrences of a value in the list
print("Number of times 101 appears in the list:", rohit_sl.count(0))
