import sys
import unittest
from typing import *
from dataclasses import dataclass
import time
import math
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(10**6)
from bst import *
# Modified TREES_PER_RUN to fit 2.5sec+ insertion times on larger sized BST's on insertion
TREES_PER_RUN : int = 9700

def example_graph_creation() -> None:
    # Return log-base-2 of 'x' + 5.

    def f_to_graph( x : float ) -> float:
        return math.log2( x ) + 5.0

    # here we're using "list comprehensions": more of Python's
    # syntax sugar.
    x_coords : List[float] = [ float(i) for i in range( 1, 100 ) ]
    y_coords : List[float] = [ f_to_graph( x ) for x in x_coords ]
    # Could have just used this type from the start, but I want
    # to emphasize that 'matplotlib' uses 'numpy''s specific array
    # type, which is different from the built-in Python array
    # type.
    x_numpy : np.ndarray = np.array( x_coords )
    y_numpy : np.ndarray = np.array( y_coords )
    plt.plot( x_numpy, y_numpy, label = 'log_2(x)' )
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Example Graph")
    plt.grid(True)
    plt.legend() # makes the 'label's show up
    plt.show()

# Defines a comes_before function for ordering
def comes_before(a: Any, b: Any) -> bool:
  return a < b

# Generates a random binary search tree with n_max nodes with insertion
def random_tree(n_max: int) -> BinarySearchTree:
    new_tree = BinarySearchTree(comes_before, None)
    for i in range(n_max):
        new_tree = insert(new_tree, random.random())
    return new_tree

# Calculates the height of a binary tree
def height(bst: Bintree) -> int:
    if bst is None:
        return 0
    return 1 + max(height(bst.left), height(bst.right))

# Measures the average height of random binary search trees of varying sizes
def height_trees_perf() -> None:
    avg_heights : List[float] = []
    for i in range(51):
        run_heights : List[int] = []
        for n in range(TREES_PER_RUN):
            run_heights.append(height(random_tree(i).tree))
        avg_heights.append(sum(run_heights) / len(run_heights))

    plt.plot( [i for i in range(51)], avg_heights, label = 'Average Height' )
    plt.xlabel("Number of Nodes")
    plt.ylabel("Average Height")
    plt.title("Average Height of Random Binary Search Trees")
    plt.grid(True)
    plt.legend()
    plt.show()

# Measures the average insertion time of random binary search trees of varying sizes
def insertion_trees_perf() -> None:
    height_list : List[float] = []
    for i in range(51):
        time1 = time.perf_counter()
        for n in range(TREES_PER_RUN):
            insert(random_tree(i), random.random())
        time2 = time.perf_counter()
        height_list.append(time2 - time1)

    plt.plot( [i for i in range(51)], height_list, label = f'Insertion Time of New Nodes w/ TREES_PER_RUN = {TREES_PER_RUN}' )
    plt.xlabel("Number of Nodes (N)")
    plt.ylabel("Insertion Time (seconds)")
    plt.title("Insertion Time of Random Value into N-sized Random Binary Search Trees")
    plt.grid(True)
    plt.legend()
    plt.show()

if (__name__ == '__main__'):
    # time1 = time.perf_counter()
    # for i in range(TREES_PER_RUN):
    #     insert(random_tree(50), random.random()) #50 is the n_max
    # time2 = time.perf_counter()
    # print(f"Time taken for example_graph_creation: {time2 - time1} seconds")

    insertion_trees_perf()
    #random_tree(1000)