import numpy as np

def dynamic_checkerboard(n):
    """
    Create an n x n checkerboard pattern using NumPy, where n is given by the user.
    """
    # Initialize an n x n array of zeros
    board = np.zeros((n, n), dtype=int)
    
    # Use slicing to set the required indices to 1
    board[1::2, ::2] = 1  # Set 1s for even-indexed rows on odd-indexed columns
    board[::2, 1::2] = 1  # Set 1s for odd-indexed rows on even-indexed columns
    
    return board

# Example for a 5x5 matrix
checkerboard_pattern_dynamic = dynamic_checkerboard(5)
print(checkerboard_pattern_dynamic)
