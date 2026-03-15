"""
Implement array and matrix operations from scratch using Python lists.
This provides a look at how data structures manage memory and indexing.
"""

from __future__ import annotations
from typing import Any, List


class Array:
    """Simple dynamic array wrapper supporting insert, delete, and access."""

    def __init__(self, initial: List[Any] | None = None) -> None:
        # Initialize with provided list or an empty one if None
        self.data = list(initial) if initial is not None else []

    def insert(self, index: int, value: Any) -> None:
        """Insert a value at a specific index by 'splitting' the array."""
        if index < 0 or index > len(self.data):
            raise IndexError("Array index out of range.")
        
        # Manual insertion: slice everything before the index, add the value,
        # and then add everything from the index to the end.
        self.data = self.data[:index] + [value] + self.data[index:]

    def append(self, value: Any) -> None:
        """Add an element to the very end of the array."""
        self.data.append(value)

    def delete(self, index: int) -> Any:
        """Remove and return the element at the given index."""
        if index < 0 or index >= len(self.data):
            raise IndexError("Array index out of range.")
            
        removed = self.data[index]
        # Rebuild the list by skipping the element at 'index'
        self.data = self.data[:index] + self.data[index + 1 :]
        return removed

    def access(self, index: int) -> Any:
        """Retrieve a value at a specific index with bounds checking."""
        if index < 0 or index >= len(self.data):
            raise IndexError("Array index out of range.")
        return self.data[index]

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        return f"Array({self.data})"

class Matrix:
    """
    Matrix implemented as a 'List of Lists'.
    The outer list represents rows; the inner lists represent columns.
    """

    def __init__(self, rows: int, cols: int, default: Any = 0) -> None:
        """Create a rows x cols matrix filled with a default value."""
        if rows <= 0 or cols <= 0:
            raise ValueError("Matrix dimensions must be positive.")
        
        # Use nested list comprehension to build the grid
        self.data = [[default for _ in range(cols)] for _ in range(rows)]

    def access(self, row: int, col: int) -> Any:
        """Get the value at a specific grid coordinate (row, col)."""
        return self.data[row][col]

    def update(self, row: int, col: int, value: Any) -> None:
        """Change the value at a specific grid coordinate."""
        self.data[row][col] = value

    def insert_row(self, index: int, row_values: List[Any] | None = None) -> None:
        """Add a new horizontal row at the specified index."""
        cols = len(self.data[0])
        
        # Default to a row of zeros if no values are provided
        if row_values is None:
            row_values = [0] * cols
        
        # Ensure the new row fits the width of the existing matrix
        if len(row_values) != cols:
            raise ValueError("Inserted row must match matrix column count.")
            
        self.data.insert(index, row_values)

    def delete_row(self, index: int) -> List[Any]:
        """Remove an entire row and return it."""
        return self.data.pop(index)

    def insert_col(self, index: int, col_values: List[Any] | None = None) -> None:
        """Add a new vertical column. This requires updating every single row."""
        rows = len(self.data)
        
        if col_values is None:
            col_values = [0] * rows
            
        if len(col_values) != rows:
            raise ValueError("Inserted column must match matrix row count.")
        
        # Loop through each row and insert the new column value at the right spot
        for row_index, value in enumerate(col_values):
            self.data[row_index].insert(index, value)

    def delete_col(self, index: int) -> List[Any]:
        """Remove a vertical column by popping from every row."""
        removed = []
        for row in self.data:
            removed.append(row.pop(index))
        return removed

    def shape(self) -> tuple[int, int]:
        """Return the dimensions as (rows, columns)."""
        return len(self.data), len(self.data[0])

    def __repr__(self) -> str:
        # Pretty-print the matrix for easier reading
        return "Matrix(\n  " + "\n  ".join(str(row) for row in self.data) + "\n)"

if __name__ == "__main__":
    # --- Array Demo ---
    array = Array([10, 20, 30])
    print("Array before operations:", array)
    array.insert(1, 15)  # Result: [10, 15, 20, 30]
    print("Array after Insertion:", array)
    array.append(40)     # Result: [10, 15, 20, 30, 40]
    print("Array after Append:", array)
    removed = array.delete(2) # Removes '20'
    print("Array after Deletion:", array)
    print("Removed element:", removed)
    # --- Matrix Demo ---
    matrix = Matrix(2, 3, default=0)
    matrix.update(0, 1, 5)        # Set top row, middle col to 5
    matrix.insert_row(1, [7, 8, 9]) # Add row in the middle
    matrix.insert_col(2, [1, 2, 3]) # Add a column near the end
    print("\nMatrix after operations:")
    print(matrix)