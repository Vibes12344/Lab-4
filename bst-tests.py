import math
import sys
import unittest
from typing import *
from dataclasses import dataclass
sys.setrecursionlimit(10**6)
from bst import *


def comes_before(a: Any, b: Any) -> bool:
  return a < b

# data defintion for Point2
@dataclass(frozen = True)
class Point2:
     x : float
     y : float

def point_dist(pt1 : Point2, pt2 : Point2) -> bool:
  return comes_before(math.sqrt(math.pow(pt1.x, 2) + math.pow(pt1.y, 2)), math.sqrt(math.pow(pt2.x, 2) + math.pow(pt2.y, 2)))


order_chars : BinarySearchTree = BinarySearchTree(comes_before, Node("d", 
                                                                          Node("b", 
                                                                              Node("a", None, None), 
                                                                              Node("c", None, None)), 
                                                                          Node("i", 
                                                                              Node("f", None, None), 
                                                                              Node("q", None, None))
                                                                        ))
order_nums : BinarySearchTree = BinarySearchTree(comes_before, Node(16, 
                                                                  Node(6, 
                                                                        Node(2, None, None), 
                                                                        None), 
                                                                  Node(75, 
                                                                        Node(18, None, None), 
                                                                        Node(81, None, None))
                                                                  ))
  
dist_bst : BinarySearchTree = BinarySearchTree(point_dist, Node(Point2(3, 4), 
                                                                  Node(Point2(0, 1), 
                                                                     None, 
                                                                     Node(Point2(2, 3), 
                                                                          None, 
                                                                          None)
                                                                  ),
                                                                  Node(Point2(1, 8), 
                                                                       None, 
                                                                       None)))


class BSTTests(unittest.TestCase):
  def test_is_empty(self):
    self.assertEqual(False, is_empty(order_nums))
    self.assertEqual(True, is_empty(BinarySearchTree(comes_before, None)))

  def test_num(self):
    # Insert test
    new_num : BinarySearchTree = BinarySearchTree(comes_before, None)
    for n in [16, 6, 2, 75, 18, 81]:
      new_num : BinarySearchTree = insert(new_num, n)
    self.assertEqual(order_nums, new_num)

    self.assertEqual(True, lookup(order_nums, 18))
    self.assertEqual(True, lookup(order_nums, 2))
    self.assertEqual(False, lookup(order_nums, 67))

    # testing delete function
    del_num = BinarySearchTree(comes_before, None)
    for n in [16, 6, 8, 75, 2, 18, 81]:
          del_num = insert(del_num, n)
    self.assertEqual(order_nums, delete(del_num, 8))

  def test_alph(self):
    # testing insert function
    new_alph = BinarySearchTree(comes_before, None)
    for n in ['d', 'b', 'a', 'c', 'i', 'f', 'q']:
          new_alph = insert(new_alph, n)
    self.assertEqual(order_chars, new_alph)

    # testing lookup function
    self.assertEqual(True, lookup(order_chars, 'c'))
    self.assertEqual(True, lookup(order_chars, 'q'))
    self.assertEqual(False, lookup(order_chars, 'e'))
    # testing delete function
    del_alph = BinarySearchTree(comes_before, None)
    for n in ['d', 'b', 'a', 'c', 'i', 'f', 'q']:
          del_alph = insert(del_alph, n)
    self.assertEqual(order_chars, delete(del_alph, 'p'))

  def test_dist(self):
    # testing insert function
    new_dist = BinarySearchTree(point_dist, None)
    for n in [Point2(3, 4), Point2(0, 1), Point2(2, 3), Point2(1, 8)]:
        new_dist = insert(new_dist, n)
    self.assertEqual(dist_bst, new_dist)

    # testing lookup function
    self.assertEqual(True, lookup(dist_bst, Point2(0, 1)))
    self.assertEqual(True, lookup(dist_bst, Point2(1, 8)))
    self.assertEqual(False, lookup(dist_bst, Point2(1, 2)))
    # testing delete function
    del_dist = BinarySearchTree(point_dist, None)
    for n in [Point2(3, 4), Point2(0, 1), Point2(2, 3), Point2(1, 8), Point2(4, 1)]:
        del_dist = insert(del_dist, n)
    self.assertEqual(dist_bst, delete(del_dist, Point2(4, 1)))

  def test_example(self):
    pass


if (__name__ == '__main__'):
  unittest.main()
