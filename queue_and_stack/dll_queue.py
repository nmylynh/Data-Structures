import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Queue:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

# function to add an element data in the Queue

  def enqueue(self, value):
    self.storage.add_to_tail(value)
  
# function to remove first element and return the element from the queue

  def dequeue(self):
    if self.storage.head == None:
      return None  
    else:
      return self.storage.remove_from_head()
      
# returns the size of the queue

  def len(self):
    return self.storage.length
