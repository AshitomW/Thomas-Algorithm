# Tridiagonal Matrix Solver

A Python implementation of the Thomas Algorithm (also known as the tridiagonal matrix algorithm) for efficiently solving tridiagonal linear systems.

## Overview

This solver implements the Thomas Algorithm to solve a tridiagonal system of linear equations of the form Ax = d, where A is a tridiagonal matrix. The algorithm runs in O(n) time complexity, making it significantly more efficient than general matrix inversion methods.

## Requirements

- Python 3.x
- NumPy

## Installation

```bash
pip install numpy
```

## Usage

```python

# Define your tridiagonal system
a = [0, -1, -1]    # lower diagonal
b = [4, 4, 4]      # main diagonal
c = [-1, -1, 0]    # upper diagonal
d = [2, 4, 10]     # right-hand side vector

# Solve the system
X = thomas(a, b, c, d)
print("Solution vector:", X)
```

## Function Description

```python
def thomas(a, b, c, d):
    """
    Solves a tridiagonal system using the Thomas algorithm.
    
    Parameters:
    a (array_like): Lower diagonal elements (first element should be 0)
    b (array_like): Main diagonal elements
    c (array_like): Upper diagonal elements (last element should be 0)
    d (array_like): Right-hand side vector
    
    Returns:
    numpy.ndarray: Solution vector X
    """
```

## Mathematical Form

The system being solved is of the form:

```
[b₁ c₁  0  0 ] [x₁]   [d₁]
[a₂ b₂ c₂  0 ] [x₂] = [d₂]
[0  a₃ b₃ c₃ ] [x₃]   [d₃]
[0   0 a₄ b₄ ] [x₄]   [d₄]
```

## Example

```python
# Example of a 3x3 system
a = [0, -1, -1]    # Lower diagonal
b = [4, 4, 4]      # Main diagonal
c = [-1, -1, 0]    # Upper diagonal
d = [2, 4, 10]     # Right-hand side

# This represents the system:
# [4  -1   0][x₁]   [2 ]
# [-1  4  -1][x₂] = [4 ]
# [0  -1   4][x₃]   [10]

X = thomas(a, b, c, d)
print("The Values of X are:", X)
```

## Algorithm Steps

1. **Forward Sweep:**
   - Modifies the coefficients starting from the first row
   - Eliminates the lower diagonal elements
   
2. **Backward Substitution:**
   - Calculates the solution starting from the last element
   - Works backwards to find all values of X

## Limitations

- The system must be diagonally dominant for numerical stability
- Input arrays must be of equal length
- First element of lower diagonal (a) must be 0
- Last element of upper diagonal (c) must be 0


## References

- [Thomas Algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm)
- [Tridiagonal Matrix (Wikipedia)](https://en.wikipedia.org/wiki/Tridiagonal_matrix)
