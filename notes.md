# CS21 Data Structures: Linked Lists w/ Brian Doyle

 [<img src="https://3.bp.blogspot.com/-sXOQBd_OCR8/WBBn3QNhOiI/AAAAAAAAALQ/ysaUNOhKMoY59zw2cRxcHioHzdvn8HdNgCLcB/s1600/simpleLinkedList.png"/>](https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/)
### Terms:

#### Array:
- An `array` is consecutive memory, and has indices. Arrays start at 0.
- arrays must be in a continuous spot in memory
    - because the index is simply multiplied by the size of the data structure
    - When we look up an array, like my_array[7], what you're doing is multiplying the size of whatever our data is in that array times the index
- Spots in memory can only be 0 or 1. There is no way to actually make it null(Delete it). 0 is a value. Null is actually a value too. 
    - You just actually remove the pointer to the data block
    - In order to pop something out of an array in the memory you have to reindex everything
    - So you can't really delete something. You're just not using it, reserving the rest of the space for use
    - deleted things aren't really deleted unless they're written over
- As you append to an array, you use up more of your allocation

     - However, when you are maxxed out in memory for an array, and you cannot allocate it future in the same data structure (because the rest of the space is for another data structure, reserved and blocked off), you must copy the existing array and allocate the copied array somewhere else in memory, **and then** you can add the new input inside the copied array.
- Basically there are different addresses for arrays in RAM
- You can put dynamic information in an array only if they're all objects.
- But you cannot put different data types into an array.
    - This is because it's how indexing works-- 
    - it's counting the bits, the actual ones and zeros to figure out where things are
    - it's just reading what happens to be there in memory
    - and you have to keep it ordered because there's no way to index things of different sizes

#### Dynamic Array:
- An array of which the size can change
- Where you can allocate more space for the same data structure

#### Queues & Stacks

- **Queues:** First in, First Out - Horizontal
    - A queue is a container of objects (a linear collection) that are inserted and removed according to the FIFO principle
    - For example, line at groceries, food courts, or retail stores
    - Only two operations are allowed:
        - **Enqueue**: Insert an item nto the back of the queue 
        - **Dequeue**: Removes the front item of the queue
    - **Applications**:
        - Await functions
        - Requests to server
        - Sorting
    - The _data type queue_ is an adapter class
        - Meaning it is built on top of data structures
        - Underlying structure for a queue could be an array, a Vector, an ArrayList, a LinkedList, or any other collection


- **Stacks:** Last In, First Out - Vertical 
    - A stack is a limited access data structure
        - Elements can only be added and removed at the top
    - Like a stack of books, you remove the top stack, and when you add, you add to the top stack
    - In _pushdown_ stacks, only two operations are allowed:
        - **push**: adds the the item into the top of the stack
        - **pop**: removes the item out of the top of the stack
    - **Applications**:
        - Reversing a word. _Push_ letter by letter, and _Pop_ letter by letter
            - _push_ `A, P, P, L, E`, _pop_ `E, L, P, P, A`
        - Undo mechanism in text editors. 
            - Keeping all text changes in a stack
            - `Ctrl + Z` 



# Linked List:

- For storage, an array isnt a good choice (cuz it's static) because you're reguarly adding and removing things
- A linked list is better, which is also a linear data structure
- A linked list is a list of nodes and they're conceptually stored linearly in memory
- In it's most basic form, a linked list is a string of nodes, sort of like a string of pearls, with each node containing both data and a reference to the next node in the list     
    - Note: This is a singly linked list. 
        - The nodes in a doubly linked list will contain references to both the next node and the previous node. 
- The main advantage of using a linked list over a similar data structure, like the static array, is the linked list’s dynamic memory allocation: 
    - if you don’t know the amount of data you want to store before hand, the linked list can adjust on the fly.* 
    - Of course this advantage comes at a price: dynamic memory allocation requires more space and commands slower look up times.

*In practice this means certain insertions are more expensive. For example, if the list initially allocates enough space for eight nodes, on the ninth insertion the list will have to double its allocated space to 16 and copy over the original 8 nodes, a more expensive operation than a normal insertion.

### Pro's and Cons, Linked List:

- If you want to delete data, or a node, you just have to unallocate it.
    - If the node was the head, you would reassign the head to the next node
    - the operation is quick, so it's `O(1)`
    - Same thing with tail
- However, if you want to lookup data, it's going to be `O(n)` (as the search iterates over each element to find it)
    - Because it's not indexed
- Linked lists prevents _buffer overflow attacks_ for when you're accessing indices in older languages
    - it prevents someone from accessing indices they're not supposed to access
- **Singly Linked Lists** are more memory efficient because it only needs one pointer
- **Doubly Linked Lsits** Needs two pointers

## The Node:

The node is where data is stored in the linked list (they remind me of those plastic Easter eggs that hold treats). Along with the data each node also holds a pointer, which is a reference to the next node in the list. Below is a simple implementation.

```python
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
```

- The node initializes with a single datum
- its pointer is set to `None` by default 
    - (this is because the first node inserted into the list will have nothing to point at!). 
- We also add a few convenience methods: 
    - `get_data`: returns the stored data
    - `get_next`: returns the next node (the node to which the object node points)
    - `set_next`: a method to reset the pointer to a new node. 

These will come in handy when we implement the Linked List.

Note: A doubly-linked list has pointers on both sides rather than a singly which has a one way pointer.

## The Linked List

A simple implementation of a linked list includes the following methods:

- **Insert:** inserts a new node into the list

- **Size:** returns size of list

- **Search:** searches list for a node containing the requested data and returns that node if found, otherwise raises an error

- **Delete:** searches list for a node containing the requested data and removes it from list if found, otherwise raises an error

## Doubly Linked List

It's better to implement a Doubly Linked List because we know what's before and what's next.

