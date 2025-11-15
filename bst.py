import sys
from typing import Any, Optional, Callable, TypeAlias
from dataclasses import dataclass

sys.setrecursionlimit(10**6)

@dataclass(frozen=True)
class Node:
    value: Any
    left: Optional["Node"] = None
    right: Optional["Node"] = None

Bintree: TypeAlias = Optional["Node"]

# A value a should come before b if this returns True
ComesBefore: TypeAlias = Callable[[Any, Any], bool]

@dataclass(frozen=True)
class BinarySearchTree:
    function: ComesBefore
    tree: Bintree = None

def is_empty(bst: BinarySearchTree) -> bool:
    return bst.tree is None

def insert_node(t: Bintree, x: Any, comes_before: ComesBefore) -> Bintree:
    if t is None:
        return Node(x)
    if comes_before(x, t.value):
        return Node(t.value, insert_node(t.left, x, comes_before), t.right)
    else:
        # if equal OR greater, go right 
        return Node(t.value, t.left, insert_node(t.right, x, comes_before))
    
def insert(bst: BinarySearchTree, x: Any) -> BinarySearchTree:
    return BinarySearchTree(
        function=bst.function,
        tree= insert_node(bst.tree, x, bst.function),
    )
def eq(a: Any, b: Any, comes_before: ComesBefore) -> bool:
    return not comes_before(a, b) and not comes_before(b, a)

def lookup_node(t: Bintree, x: Any, comes_before: ComesBefore) -> bool:
    while t is not None:
        if eq(x, t.value, comes_before):
            return True
        t = t.left if comes_before(x, t.value) else t.right
    return False 

def lookup(bst: BinarySearchTree, x: Any) -> bool:
    return lookup_node(bst.tree, x, bst.function)

def delete(bst: BinarySearchTree, x: Any) -> BinarySearchTree:
    def delete_node(t: Bintree, x: Any, comes_before: ComesBefore) -> Bintree:
        if t is None:
            return None
        if eq(x, t.value, comes_before):
            if t.left is None:
                return t.right
            if t.right is None:
                return t.left
            # Node with two children: Get the inorder successor (smallest in the right subtree)
            successor = t.right
            while successor.left is not None:
                successor = successor.left
            # Delete the inorder successor and replace t's value with it
            return Node(successor.value, t.left, delete_node(t.right, successor.value, comes_before))
        elif comes_before(x, t.value):
            return Node(t.value, delete_node(t.left, x, comes_before), t.right)
        else:
            return Node(t.value, t.left, delete_node(t.right, x, comes_before))
    
    return BinarySearchTree(
        function=bst.function,
        tree=delete_node(bst.tree, x, bst.function),
    )