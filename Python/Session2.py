# Assuming the 'cars' tuple is defined somewhere earlier, like:
cars = ("Toyota", "BMW", "Audi", "Renault")

# Length of the tuple
print("No of items in the cars tuple is", len(cars))

# Accessing the 2nd car (index 1)
print("2nd car model in the cars:", cars[1])

# Tuples are immutable, so this line would cause an error if uncommented:
# cars[1] = "Maruti"

# Using a for loop to print each car
for x in range(len(cars)):
    print(cars[x])

# Alternative way to loop through the tuple
for car in cars:
    print(car)

# Slicing the tuple
print("FIRST TWO CARS:", cars[:2])  # First two cars
print("All cars skipping TWO CARS:", cars[2:])  # All cars except the first two
print("All cars except the last one:", cars[:-1])  # All cars except the last
print("Only the last car:", cars[-1:])  # Only the last car
print("All cars between 2nd and 3rd position:", cars[1:3])  # Between 2nd and 3rd position

# Counting occurrences of "BMW"
print("Count of BMW in the cars:", cars.count("BMW"))

# Checking if "Renault" is in the cars tuple
print("Existence of model Renault:", "Renault" in cars)

# Finding the index of "Toyota"
print("The index of Toyota car is", cars.index("Toyota"))

# Concatenating a tuple (trucks)
trucks = ("Volvo",)
vehicles = cars + trucks  # Concatenate cars and trucks

# Print the concatenated tuple
print(vehicles)
