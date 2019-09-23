import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# `insert` adds the input value to the binary search tree, adhering to the rules of the ordering of elements in a binary search tree.

# traverse tree by recursion
  
  def insert(self, value):
    if value < self.value: # input < parent?
      if self.left != None: # input isn't None?
        self.left.insert(value) # insert to left
      else:
        self.left = BinarySearchTree(value) # is none? new node
    elif value > self.value:
      if self.right != None: 
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
  

# `contains` searches the binary search tree for the input value, returning a boolean indicating whether the value exists in the tree or not.

  def contains(self, target):
    if target == self.value:
      return True
    elif self.value > target:
      self.contains(self.right)
    elif self.value < target:
      self.contains(self.left)
    else:
      return False

# `get_max` returns the maximum value in the binary search tree.

  def get_max(self):
    pass

# `for_each` performs a traversal of _every_ node in the tree, executing the passed-in callback function on each tree node value. There is a myriad of ways to perform tree traversal; in this case any of them should work. 

  def for_each(self, cb):
    pass