# Assignment 11 :
# Apply Pandas to create a Series containing ten random numbers and 
# perform indexing, filtering, and statistical operations 
# such as mean, median, minimum, and maximum.

import pandas as pd
import numpy as np

# Generate 10 random numbers between 1 and 100
numbers = np.random.randint(1, 101, 10)

# Create a Pandas Series from the random numbers
s = pd.Series(numbers)
print("Original Series:")
print(s)

# Access an element using its index
print("\nElement at index 2:", s[2])

# Filter and display numbers greater than 50
print("\nNumbers greater than 50:")
print(s[s > 50])

# Calculate statistical measures
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())
