# Assignment 6: Medians and Order Statistics & Elementary Data Structures


## Overview

This repository contains the implementation and analysis for **Assignment 6: Medians and Order Statistics & Elementary Data Structures**.

The assignment is divided into two parts:

- **Part 1:** Implementation and analysis of selection algorithms for finding the **kth smallest element** in an array
- **Part 2:** Implementation and discussion of fundamental data structures such as arrays, stacks, queues, and linked lists

This project combines algorithm design, complexity analysis, empirical evaluation, and data structure implementation from scratch in Python.

---

## Assignment Objectives

The main goals of this assignment are:

- to implement deterministic and randomized selection algorithms
- to analyze their theoretical time and space complexity
- to compare their practical performance experimentally
- to implement basic data structures from scratch in Python
- to study the trade-offs and real-world applications of these data structures

---

## Repository Structure

```text

├── part1_selection/
│   ├── deterministic_selection.py
│   ├── randomized_selection.py
│   └── benchmark.py
│
├── part2_data_structures/
│   ├── arrays_matrices.py
│   ├── stack.py
│   ├── queue.py
│   ├── linked_list.py
│   └── rooted_tree.py
│
├── Assignment_6_Report.docx
│   
└── README.md
```


---

## Technologies Used

- **Language:** Python 3.x
- **Standard Libraries Used:**
  - `random`
  - `time`


---

## How to Run the Project


### Part 1: Selection Algorithms

```bash
cd part1_selection
python deterministic_selection.py
python randomized_selection.py
python benchmark.py
```

### Part 2: Elementary Data Structures

```bash
cd part2_data_structures
python arrays_matrices.py
python stack.py
python queue.py
python linked_list.py
python rooted_tree.py
```


---

## Part 1: Selection Algorithms

**order statistics problem**, specifically finding the **kth smallest element** in an array efficiently.

### Deterministic Selection

The deterministic selection algorithm is implemented using the **Median of Medians** method.

#### Key Characteristics

- worst-case time complexity: **O(n)**
- uses a carefully selected pivot
- divides the array into groups of five
- supports duplicate elements using **three-way partitioning**
- provides strong theoretical guarantees

This method is useful when worst-case performance must remain predictable and reliable.

### Randomized Selection

The randomized selection algorithm is implemented using **Randomized Quickselect**.

#### Key Characteristics

- expected time complexity: **O(n)**
- worst-case time complexity: **O(n²)**
- chooses the pivot randomly
- generally faster in practice due to lower constant overhead
- also uses **three-way partitioning** to handle duplicates efficiently

This method is often preferred in practice because it is simple and performs well on average.

### Edge Cases Handled

The implementations are designed to handle:

- arrays with duplicate values
- single-element arrays
- invalid values of `k`
- empty arrays

### Benchmarking Approach

The `benchmark.py` file compares the deterministic and randomized algorithms on:

- random arrays
- sorted arrays
- reverse-sorted arrays


---

## Part 2: Elementary Data Structures

Implementing basic data structures from scratch and analyzing their efficiency and practical use.

### Arrays and Matrices

This implementation includes core array and matrix operations such as:

- insertion
- deletion
- access
- update of matrix elements
- row and column handling where applicable

Arrays are efficient for direct indexed access, while matrices are useful for representing two-dimensional structured data.

### Stack

The stack is implemented using arrays and supports:

- `push()`
- `pop()`
- `peek()`
- `is_empty()`

This follows the **LIFO (Last-In, First-Out)** principle.

### Queue

The queue is implemented using arrays and supports:

- `enqueue()`
- `dequeue()`
- `front()`
- `is_empty()`

This follows the **FIFO (First-In, First-Out)** principle.

A circular-array style approach is preferred because it avoids inefficient element shifting.

### Singly Linked List

The singly linked list implementation includes:

- insertion
- deletion
- traversal

Each node stores:

- a value
- a reference to the next node


### Rooted Tree

An rooted tree implementation is included to represent hierarchical data using linked nodes.

This is useful for modeling structures such as:

- file systems
- organizational hierarchies
- nested documents

---

## Performance Summary

### Selection Algorithms

| Algorithm | Best / Expected Time | Worst-Case Time | Notes |
|---|---:|---:|---|
| Deterministic Selection | O(n) | O(n) | Strong worst-case guarantee |
| Randomized Selection | O(n) expected | O(n²) | Faster in practice on average |

### Data Structures

| Data Structure | Access | Insert | Delete | Remarks |
|---|---:|---:|---:|---|
| Array | O(1) | O(n) in the middle | O(n) in the middle | Fast indexing |
| Matrix | O(1) element access | Depends on operation | Depends on operation | Good for 2D data |
| Stack | O(1) | O(1) | O(1) | Efficient LIFO operations |
| Queue | O(1) | O(1) | O(1) | Efficient with circular indexing |
| Singly Linked List | O(n) | O(1) at head | O(1) at head / O(n) if search is needed | Flexible structure |

---

## Real-World Applications

### Arrays and Matrices

Used in:

- tabular data representation
- image processing
- scientific computing
- sensor data storage
- dynamic programming tables

### Stacks

Used in:

- function call management
- undo and redo systems
- compiler parsing
- expression evaluation
- browser history

### Queues

Used in:

- task scheduling
- printer job handling
- breadth-first search
- customer support systems
- distributed message processing

### Linked Lists

Used in:

- graph adjacency lists
- hash-table collision handling
- memory management systems
- dynamic playlists
- applications with frequent updates

---

## Summary of Findings

This project demonstrates that efficient problem solving depends on choosing the right algorithm and the right data structure for a given situation.

### Key Findings from Part 1

- both selection algorithms scale approximately linearly in practical testing
- the randomized algorithm generally performs faster in practice
- the deterministic algorithm is more theoretically robust because it guarantees worst-case **O(n)** time
- the randomized algorithm remains attractive because of its lower practical overhead

### Key Findings from Part 2

- arrays are best when fast indexed access is required
- linked lists are more suitable when insertions and deletions are frequent
- stacks are ideal for LIFO-based tasks
- queues are ideal for FIFO-based tasks

---



## Author

**Pranavi Balakulla**
