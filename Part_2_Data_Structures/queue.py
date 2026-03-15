"""Array-based queue implementation using a circular array."""

from __future__ import annotations

from typing import Any, List


class Queue:
    def __init__(self, capacity: int = 10) -> None:
        # Ensure that the queue starts with a valid positive capacity
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")

        # Create the underlying array and initialize queue state
        self._data: List[Any | None] = [None] * capacity
        self._front = 0
        self._size = 0

    def _resize(self) -> None:
        # Double the capacity when the queue becomes full
        new_capacity = len(self._data) * 2
        new_data: List[Any | None] = [None] * new_capacity

        # Copy elements to the new array in their logical queue order
        for i in range(self._size):
            new_data[i] = self._data[(self._front + i) % len(self._data)]

        # Replace the old array and reset the front index
        self._data = new_data
        self._front = 0

    def enqueue(self, value: Any) -> None:
        # Resize the array if there is no free space left
        if self._size == len(self._data):
            self._resize()

        # Find the next available position at the rear of the queue
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = value
        self._size += 1

    def dequeue(self) -> Any:
        # Do not allow removal from an empty queue
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        # Remove and return the front element
        value = self._data[self._front]
        self._data[self._front] = None

        # Move the front pointer forward using circular indexing
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return value

    def front(self) -> Any:
        # Return the front element without removing it
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self._data[self._front]

    def is_empty(self) -> bool:
        # The queue is empty when its size is zero
        return self._size == 0

    def size(self) -> int:
        # Return the number of elements currently in the queue
        return self._size

    def __repr__(self) -> str:
        # Build a list of items in logical queue order for display
        items = [self._data[(self._front + i) % len(self._data)] for i in range(self._size)]
        return f"Queue({items})"


if __name__ == "__main__":
    # Example usage of the queue
    queue = Queue(capacity=3)

    queue.enqueue("A")
    queue.enqueue("B")
    queue.enqueue("C")

    print("Queue after enqueues:", queue)
    print("Front element:", queue.front())
    print("Dequeued element:", queue.dequeue())

    queue.enqueue("D")
    print("Queue now:", queue)