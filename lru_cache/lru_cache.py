from doubly_linked_list import DoublyLinkedList
class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.

  """

# Need a DLL to store the order
# Dict store key value pairs
# need two things for size:
# currrent size & limit

  def __init__(self, limit=10):
    self.order = DoublyLinkedList()
    self.storage = dict()
    self.size = 0
    self.limit= limit

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    pass

  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """


  # Add pair to the cache - add to dict and add it to nodes/DLL
  def set(self, key, value):
    # if already exist, overwrite value 
    if key in self.storage:
    # - update dict
      node = self.storage[key]
      node.value = (key, value)
    # mark as most recently used - Put in the head of the DLL
      self.order.move_to_front(node)
      return
    # if at max capacity, dump oldest - remove from tail of DLL
    if self.size == self.limit:
    # dump the oldest:
    # remove it from the linked list
    # remove it from the dict
      del self.storage[self.order.tail.value[0]]
      self.order.remove_from_tail()
      self.size -= 1
    # add pair to the cache - add to dict and add it to nodes/DLL
    self.order.add_to_head((key, value))
    self.storage[key] = self.order.head
    self.size += 1



