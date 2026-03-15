"""
Deterministic selection using the Median of Medians technique.
This module finds the k-th smallest element (1-based indexing) in O(n) time.
"""

from __future__ import annotations
from typing import List, Sequence, TypeVar

T = TypeVar("T")


class SelectionError(ValueError):
    """Raised when an invalid k value is given to a selection function."""


def deterministic_select(values: Sequence[T], k: int) -> T:
    """
    Return the k-th smallest element of values using 1-based indexing.
    """
    # Reject empty input because no order statistic can be selected.
    if not values:
        raise SelectionError("Cannot select from an empty sequence.")

    # Reject invalid values of k.
    if k < 1 or k > len(values):
        raise SelectionError(f"k must be between 1 and {len(values)}.")

    # Convert the input to a list so the original sequence is not modified,
    # and change k to 0-based indexing for the helper function.
    return _select(list(values), k - 1)


def _select(arr: List[T], k_index: int) -> T:
    """Recursive helper function that works with 0-based indexing."""

    # For very small arrays, sorting directly is simpler and efficient.
    if len(arr) <= 5:
        arr.sort()
        return arr[k_index]

    # Choose a pivot using the Median of Medians method.
    pivot = _median_of_medians(arr)

    # Partition the array into three parts:
    # elements smaller than the pivot, equal to the pivot, and greater than the pivot.
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    # Decide which partition contains the desired element.
    if k_index < len(lows):
        # The target lies in the smaller elements.
        return _select(lows, k_index)
    elif k_index < len(lows) + len(pivots):
        # The target is equal to the pivot.
        return pivot
    else:
        # The target lies in the larger elements.
        # Adjust the index relative to the new subarray.
        return _select(highs, k_index - len(lows) - len(pivots))


def _median_of_medians(arr: List[T]) -> T:
    """Select a pivot deterministically using the Median of Medians strategy."""

    # Split the array into groups of at most 5 elements.
    groups = [arr[i : i + 5] for i in range(0, len(arr), 5)]

    # Compute the median of each group.
    medians: List[T] = []
    for group in groups:
        group.sort()
        medians.append(group[len(group) // 2])

    # If the number of medians is small, sort them and return the middle one.
    if len(medians) <= 5:
        medians.sort()
        return medians[len(medians) // 2]

    # Otherwise, recursively find the median of the medians.
    return _select(medians, len(medians) // 2)


if __name__ == "__main__":
    # Example test case
    sample = [12, 3, 5, 7, 4, 19, 26, 3, 7, 7, 10]
    k = 5

    result = deterministic_select(sample, k)

    print(f"Input array: {sample}")
    print(f"{k}-th smallest element: {result}")