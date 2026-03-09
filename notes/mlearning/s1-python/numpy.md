# Create
arr = np.array([1, 2, 3])

# Stats
arr.mean()    # Average
arr.sum()     # Sum
arr.max()     # Maximum
arr.min()     # Minimum
arr.std()     # Standard deviation

# Reshape
arr.reshape(3, 1)  # Change shape
arr.T              # Transpose

# Combine
np.concatenate([arr1, arr2])
np.stack([arr1, arr2])

The Main Problem NumPy Solves
Regular Python Lists (SLOW):
python
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]  # Loops through each item
# Takes 1 second for 1 million items
NumPy Arrays (FAST):
python
import numpy as np
numbers = np.array([1, 2, 3, 4, 5])
doubled = numbers * 2  # Does ALL at once!
# Takes 0.01 seconds for 1 million items
