
import numpy as np

# Create an array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# Perform slicing operations
print("First five elements:", arr[:5])
print("Elements from index 5:", arr[5:])
print("Alternate elements:", arr[::2])

# Calculate statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting: Add 5 to every element
modified_arr = arr + 5
print("Array after Broadcasting:", modified_arr)
