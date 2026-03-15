"""Singly linked list implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Node:
    # Store the value of the node and a reference to the next node
    data: Any
    next: Optional["Node"] = None


class SinglyLinkedList:
    def __init__(self) -> None:
        # Initially, the linked list is empty
        self.head: Optional[Node] = None

    def insert_at_beginning(self, value: Any) -> None:
        # Create a new node and make it the new head
        self.head = Node(value, self.head)

    def insert_at_end(self, value: Any) -> None:
        # Create a new node to be added at the end
        new_node = Node(value)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Otherwise, move to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

    def delete(self, value: Any) -> bool:
        # Start from the head and keep track of the previous node
        current = self.head
        previous: Optional[Node] = None

        # Traverse the list until the value is found or the list ends
        while current is not None:
            if current.data == value:
                # If the node to delete is the head node
                if previous is None:
                    self.head = current.next
                else:
                    # Skip the current node by changing the previous link
                    previous.next = current.next
                return True

            # Move to the next node
            previous = current
            current = current.next

        # Return False if the value is not found
        return False

    def traverse(self) -> list[Any]:
        # Collect all node values in a Python list
        elements = []
        current = self.head

        while current is not None:
            elements.append(current.data)
            current = current.next

        return elements

    def __repr__(self) -> str:
        # Return a readable string representation of the linked list
        return " -> ".join(map(str, self.traverse())) if self.head else "Empty"


if __name__ == "__main__":
    # Example usage of the singly linked list
    linked_list = SinglyLinkedList()

    linked_list.insert_at_beginning(20)
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)

    print("Linked list after insertions:", linked_list)

    deleted = linked_list.delete(30)
    print("Deleted 30?", deleted)

    print("Linked list now:", linked_list)
    print("Traversal result:", linked_list.traverse())