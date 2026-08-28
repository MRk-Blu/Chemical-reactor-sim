import numpy as np
# 1. Create a 2x3 matrix representing 2 reactors, each holding 3 different liquid volumes (Liters)
reactor_volumes = np.array([
    [100.0, 250.0, 500.0],
    [150.0, 300.0, 450.0]
])

# 2. Broadcasting: Add 50 Liters of buffer liquid to EVERY single tank
updated_volumes = reactor_volumes + 50.0

# 3. Matrix Transposition: Swap rows and columns (3 rows, 2 columns)
transposed_matrix = reactor_volumes.T

print("--- Updated Volumes (+50L) ---")
print(updated_volumes)
print(reactor_volumes)

print("\n--- Transposed Matrix Shape ---")
print("Original shape:", reactor_volumes.shape)
print("Transposed shape:", transposed_matrix.shape)
print(transposed_matrix)

# Sum across columns (axis=1) -> Total liquid volume inside each reactor
reactor_totals = reactor_volumes.sum(axis=1)

# Sum down rows (axis=0) -> Total volume of Chemical 1, Chem 2, Chem 3 across the entire plant
chemical_totals = reactor_volumes.sum(axis=0)

print("\n--- Matrix Aggregations ---")
print("Total volume per reactor:", reactor_totals)      # Output: [850. 900.]
print("Total volume per chemical:", chemical_totals)    # Output: [250. 550. 950.]
print("Total volume across all reactors:", reactor_totals.sum())  # Output: 1750.0