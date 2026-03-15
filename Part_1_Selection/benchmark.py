"""Benchmark deterministic and randomized selection algorithms.

This script compares the running time of the two implementations on random,
sorted, and reverse-sorted inputs for several input sizes.
"""

from __future__ import annotations

import random
import statistics
import time
from typing import Callable, Dict, List

from deterministic_selection import deterministic_select
from randomized_selection import randomized_select

# Type alias for selection functions that return an integer result
SelectionFn = Callable[..., int]


def make_inputs(size: int) -> Dict[str, List[int]]:
    """Create input arrays of different distributions for benchmarking."""
    random_values = random.sample(range(size * 10), size)
    return {
        "random": random_values,
        "sorted": sorted(random_values),
        "reverse_sorted": sorted(random_values, reverse=True),
    }


def time_function(func: SelectionFn, arr: List[int], k: int, repeats: int = 5) -> float:
    """Run a selection function multiple times and return the average duration."""
    durations = []

    for repeat in range(repeats):
        start = time.perf_counter()

        # Use a fixed seed for each repeat when testing the randomized version
        # so that results are reproducible across benchmark runs.
        if func is randomized_select:
            func(arr, k, seed=repeat)
        else:
            func(arr, k)

        end = time.perf_counter()
        durations.append(end - start)

    # Return the mean running time across all repetitions
    return statistics.mean(durations)


def run_benchmark() -> None:
    """Execute the benchmark and print the results in table format."""
    sizes = [1000, 5000, 10000]
    repeats = 5

    header = (
        f"{'Size':>8} | {'Distribution':>15} | "
        f"{'Deterministic (ms)':>20} | {'Randomized Avg (ms)':>21}"
    )
    print(header)
    print("-" * len(header))

    # Test each input size on all input distributions
    for size in sizes:
        datasets = make_inputs(size)

        # Select the median position as the target order statistic
        k = size // 2 if size % 2 == 0 else (size // 2) + 1

        for name, arr in datasets.items():
            # Measure average execution time for both algorithms
            det_time = time_function(
                deterministic_select, arr, k, repeats=repeats
            ) * 1000
            rand_time = time_function(
                randomized_select, arr, k, repeats=repeats
            ) * 1000

            # Print times in milliseconds
            print(f"{size:>8} | {name:>15} | {det_time:>20.3f} | {rand_time:>21.3f}")


if __name__ == "__main__":
    # Start the benchmark when the script is run directly
    run_benchmark()