"""Optional rooted tree implementation using linked nodes."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, List


@dataclass
class TreeNode:
    # Store the node value and a list of child nodes
    value: Any
    children: List["TreeNode"] = field(default_factory=list)

    def add_child(self, child: "TreeNode") -> None:
        # Add a new child node to the current node
        self.children.append(child)


class RootedTree:
    def __init__(self, root_value: Any) -> None:
        # Create the tree with a single root node
        self.root = TreeNode(root_value)

    def preorder(self) -> List[Any]:
        # Store the preorder traversal result
        result: List[Any] = []

        def _traverse(node: TreeNode) -> None:
            # Visit the current node first
            result.append(node.value)

            # Recursively visit each child node
            for child in node.children:
                _traverse(child)

        # Start traversal from the root
        _traverse(self.root)
        return result


if __name__ == "__main__":
    # Example usage of the rooted tree
    tree = RootedTree("A")

    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")

    # Build the tree structure
    tree.root.add_child(b)
    tree.root.add_child(c)
    b.add_child(d)
    b.add_child(e)

    # Print the preorder traversal
    print("Preorder traversal of rooted tree:", tree.preorder())