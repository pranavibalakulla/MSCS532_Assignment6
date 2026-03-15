"""
Randomized selection using Quickselect.
This finds the k-th smallest element in expected linear time, O(n).
"""

from __future__ import annotations
import random
from typing import List, Sequence, TypeVar

T = TypeVar("T")

class SelectionError(ValueError):
    """Custom exception for out-of-bounds or empty input errors."""

def randomized_select(values: Sequence[T], k: int, seed: int | None = None) -> T:
    """
    Public API: Finds the k-th smallest element (1-indexed).
    
    Args:
        values: The sequence to search.
        k: The rank (e.g., 1 for the smallest, len(values) for the largest).
        seed: Optional seed to make the 'random' choices repeatable for testing.
    """
    if not values:
        raise SelectionError("Cannot select from an empty sequence.")
    if k < 1 or k > len(values):
        raise SelectionError(f"k must be between 1 and {len(values)}.")

    # Initialize the random number generator
    rng = random.Random(seed)
    
    # Convert k to a 0-based index and work on a list copy
    return _quickselect(list(values), k - 1, rng)

def _quickselect(arr: List[T], k_index: int, rng: random.Random) -> T:
    """
    The recursive core of the algorithm. 
    It narrows down the search space by partitioning the array.
    """
    # Base case: if there is only one element, that must be our target
    if len(arr) == 1:
        return arr[0]

    # Step 1: Pick a random element to be the pivot.
    # This randomness is what prevents worst-case O(n^2) in most real-world data.
    pivot = rng.choice(arr)

    # Step 2: Three-way partition.
    # We group elements into those smaller, larger, or equal to the pivot.
    lows = [x for x in arr if x < pivot]      # Elements < pivot
    highs = [x for x in arr if x > pivot]     # Elements > pivot
    pivots = [x for x in arr if x == pivot]   # Elements == pivot (handles duplicates)

    # Step 3: Figure out which group contains the k-th element.
    if k_index < len(lows):
        # Target is in the 'smaller' group; search only that list.
        return _quickselect(lows, k_index, rng)
    
    elif k_index < len(lows) + len(pivots):
        # Target is one of the pivot elements! We can return it immediately.
        return pivot
    
    else:
        # Target is in the 'larger' group. 
        # We adjust the index because we've discarded 'lows' and 'pivots'.
        new_k_index = k_index - len(lows) - len(pivots)
        return _quickselect(highs, new_k_index, rng)
if __name__ == "__main__":
    sample = [12, 3, 5, 7, 4, 19, 26, 3, 7, 7, 10]
    k = 5
    # Using a seed ensures that every time you run this, you get the same 'random' path.
    result = randomized_select(sample, k, seed=42)
    print(f"Input array: {sample}")
    print(f"{k}-th smallest element (randomized): {result}")