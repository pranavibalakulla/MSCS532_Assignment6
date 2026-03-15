"""Array-based stack implementation."""

from __future__ import annotations

from typing import Any, List


class Stack:
    def __init__(self) -> None:
        # Use a Python list to store stack elements
        self._items: List[Any] = []

    def push(self, value: Any) -> None:
        # Add a new element to the top of the stack
        self._items.append(value)

    def pop(self) -> Any:
        # Do not allow removal from an empty stack
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        # Remove and return the top element
        return self._items.pop()

    def peek(self) -> Any:
        # Do not allow access to the top element if the stack is empty
        if self.is_empty():
            raise IndexError("Cannot peek into an empty stack.")

        # Return the top element without removing it
        return self._items[-1]

    def is_empty(self) -> bool:
        # The stack is empty when it contains no elements
        return len(self._items) == 0

    def size(self) -> int:
        # Return the number of elements currently in the stack
        return len(self._items)

    def __repr__(self) -> str:
        # Return a readable string representation of the stack
        return f"Stack({self._items})"


if __name__ == "__main__":
    # Example usage of the stack
    stack = Stack()

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack after pushes:", stack)
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    print("Stack now:", stack)