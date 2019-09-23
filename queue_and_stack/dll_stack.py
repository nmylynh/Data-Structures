import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# A DLL is a dynamic link library that contains code and data that can be used by more than one program at the same time. This is a shared library.
# By using a DLL, a program can be modularized into separate components.
class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_head(value)
  
  def pop(self):
    if self.storage.head == None:
      return None
    else: 
      return self.storage.remove_from_head()

  def len(self):
    return self.storage.__len__()
