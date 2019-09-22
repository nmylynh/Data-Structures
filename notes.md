# CS21 Data Structures: Linked Lists w/ Brian Doyle

 [<img src="https://3.bp.blogspot.com/-sXOQBd_OCR8/WBBn3QNhOiI/AAAAAAAAALQ/ysaUNOhKMoY59zw2cRxcHioHzdvn8HdNgCLcB/s1600/simpleLinkedList.png"/>](https://www.codefellows.org/blog/implementing-a-singly-linked-list-in-python/)

## :capital_abcd: Terms:

### :one: Array:
1.  An `array` is consecutive memory, and has indices. Arrays start at 0.
2. arrays must be in a continuous spot in memory
    - because the index is simply multiplied by the size of the data structure
    - When we look up an array, like my_array[7], what you're doing is multiplying the size of whatever our data is in that array times the index
3. Spots in memory can only be 0 or 1. There is no way to actually make it null(Delete it). 0 is a value. Null is actually a value too. 
    - You just actually remove the pointer to the data block
    - In order to pop something out of an array in the memory you have to reindex everything
    - So you can't really delete something. You're just not using it, reserving the rest of the space for use
    - deleted things aren't really deleted unless they're written over
4. As you append to an array, you use up more of your allocation

     - However, when you are maxxed out in memory for an array, and you cannot allocate it future in the same data structure (because the rest of the space is for another data structure, reserved and blocked off), you must copy the existing array and allocate the copied array somewhere else in memory, **and then** you can add the new input inside the copied array.
5. Basically there are different addresses for arrays in RAM
6. You can put dynamic information in an array only if they're all objects.
7. But you cannot put different data types into an array.
    - This is because it's how indexing works-- 
    - it's counting the bits, the actual ones and zeros to figure out where things are
    - it's just reading what happens to be there in memory
    - and you have to keep it ordered because there's no way to index things of different sizes

### :two: Dynamic Array:
- An array of which the size can change
- Where you can allocate more space for the same data structure
- Definition: a dynamic array, growable array, resizable array, dynamic table, mutable array, or array list is a random access, variable-size list data structure that allows elements to be added or removed. It is supplied with standard libraries in many modern mainstream programming languages.

### :three: Queues & Stacks
 [<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--40bG1tSg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/fcxri84smzo9m1pxbxj9.png"/>](https://dev.to/rinsama77/data-structure-stack-and-queue-4ecd)

### :restroom: **Queues:** First in, First Out - Horizontal
**A queue is a container of objects (a linear collection) that are inserted and removed according to the FIFO principle**
- For example, line at groceries, food courts, or retail stores
- Only two operations are allowed:
    - **Enqueue**: Insert an item nto the back of the queue 
    - **Dequeue**: Removes the front item of the queue
- The _data type queue_ is an adapter class
    - Meaning it is built on top of data structures
    - Underlying structure for a queue could be an array, a Vector, an ArrayList, a LinkedList, or any other collection
- _Applications_:
    - Await functions
    - Requests to server
    - Sorting

 [<img src="https://res.cloudinary.com/practicaldev/image/fetch/s--GS1k4iwx--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/l8r4ic2gedi0j9obd7ix.jpg"/>](https://dev.to/rinsama77/data-structure-stack-and-queue-4ecd)

### :books: **Stacks:** Last In, First Out - Vertical 
**A stack is a limited access data structure  where elements can only be added and removed at the top, LIFO principle**
- Like a stack of books, you remove the top stack, and when you add, you add to the top stack
- There are 3 basic operations on a stack:
    1. **Push:** Insert a data item on the stack.
    2. **Pop:** Remove an item from the top of the stack.
    3. **Peek:** Read the value of an item from the top of the stack WITHOUT removing it

- _Applications_:
    - Reversing a word. _Push_ letter by letter, and _Pop_ letter by letter
        - _push_ `A, P, P, L, E`
        - _pop_ `E, L, P, P, A`
    - Undo mechanism in text editors. 
        - Keeping all text changes in a stack
        - `Ctrl + Z` 



### :four: :link: Linked Lists:

#### A linked list is a list of nodes and they're conceptually stored linearly in memory
#### In it's most basic form, a linked list is a string of nodes, sort of like a string of pearls, with each node containing both data and a reference to the next node in the list     
1. **Singly linked lists** have one head, one tail, with each node having a one directional pointer to the _next node_.
2. **Doubly linked lists** will contain references to both the _next node_ and the _previous node._
- The main advantage of using a linked list over a similar data structure, like the static array, is the linked list’s dynamic memory allocation: 
    - if you don’t know the amount of data you want to store before hand, the linked list can adjust on the fly.* 
    - Of course this advantage comes at a price: dynamic memory allocation requires more space and commands slower look up times.
- For storage, an array isnt a good choice (cuz it's static) because you're reguarly adding and removing things, but linked list allows for effcient operations due to it's structure


*In practice this means certain insertions are more expensive. For example, if the list initially allocates enough space for eight nodes, on the ninth insertion the list will have to double its allocated space to 16 and copy over the original 8 nodes, a more expensive operation than a normal insertion.

#### :interrobang: Pro's and Cons, Linked List:

- If you want to delete data, or a node, you just have to unallocate it.
    - If the node was the head, you would reassign the head to the next node
    - the operation is quick, so it's `O(1)`
    - Same thing with tail
- However, if you want to lookup data, it's going to be `O(n)` (as the search iterates over each element to find it)
    - Because it's not indexed
- Linked lists prevents _buffer overflow attacks_ for when you're accessing indices in older languages
    - it prevents someone from accessing indices they're not supposed to access
- **Singly Linked Lists** are more memory efficient because it only needs one pointer
- **Doubly Linked Lists** Needs two pointers

##  :paperclips: Structure of Linked Lists:
### :paperclip: The Node:

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


## Implementation

A simple implementation of a linked list includes the following methods:

- **Insert:** inserts a new node into the list

- **Size:** returns size of list

- **Search:** searches list for a node containing the requested data and returns that node if found, otherwise raises an error

- **Delete:** searches list for a node containing the requested data and removes it from list if found, otherwise raises an error

### The Head:

- Is the top node in the list. 
- When the list is first initialized it has no nodes, so the head is set to None. 
- The linked list doesn’t necessarily require a node to initialize. 
    - The head argument will default to None if a node is not provided.

```python
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
```
### Insert:

**This insert method takes data, _initializes a new node_ with the given data, and _adds it to the list._** .

- This insert method is `O(1)` 
    - The insert method, no matter what, will always take the same amount of time: it can only take one data point, it can only ever create one node, and the new node doesn’t need to interact with all the other nodes in the list, the inserted node will only ever interact with the head.

```python
def insert(self, data):
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node
```

### Size:

The size method is very simple, it basically counts nodes until it can’t find any more, and returns how many nodes it found. The method starts at the head node, travels down the line of nodes until it reaches the end (the current will be None when it reaches the end) while keeping track of how many nodes it has seen.

The time complexity of size is O(n) because each time the method is called it will always visit every node in the list but only interact with them once, so n * 1 operations.

```python
def size(self):
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    return count
```
### Search:

Search is actually very similar to size, but instead of traversing the whole list of nodes it checks at each stop to see whether the current node has the requested data and if so, returns the node holding that data. If the method goes through the entire list but still hasn’t found the data, it raises a value error and notifies the user that the data is not in the list.

The time complexity of search is `O(n)`.

```python
def search(self, data):
    current = self.head
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    return current
```

### Delete:

Delete also iterates over each node as it searches for the node to be deleted. It keeps track of the node it passes, until it reaches the node to be delete and unallocates it by changing the pointer of the previous node to point to the next one.

The time complexity for delete is also O(n), because in the worst case it will visit every node, interacting with each node a fixed number of times.

```python
def delete(self, data):
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())
```

#### Random

Empty returns:

```python
if hasattr(self, 'moved_away'): # if this is True we return/end the function
        return
     # if previous statement was False we start executing code from here
```

> In class-based programming, objects are created from classes by subroutines called constructors, and destroyed by destructors. 

>An object is an instance of a class, and may be called a class instance or class object; instantiation is then also known as construction.

>self represents the instance of the class. By using the “self” keyword we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.


## Doubly Linked List

It's better to implement a Doubly Linked List because we know what's before and what's next.

### Stacks:

From GeeksforGeeks:

>A stack is a collection of objects that are inserted and removed using Last in First out Principle(LIFO). User can insert elements into the stack, and can only access or remove the recently inserted object on top of the stack.
>The main advantage of using LinkedList over array for implementing **stack** is the **dynamic allocation of data**, whereas in the array, the size of the stack is restricted and there is a chance of stack overflow error when the size of the stack is exceeded the maximum size.

### Stack Operations:

1. `push()` : Insert the element into Stack and assign the top pointer to the element.
2. `pop()` : Return top element from the Stack and move the top pointer to the
second element of the Stack.
3. `top()` : Return the top element.
4. `size()` : Return the Size of the Stack.
5. `isEmpty()` : Return True if Stack is Empty else return False.
6. `printstack()` : Print all elements of the stack.

```python
# A complete working Python program to demonstrate all  
# stack operations using a doubly linked list  
  
# Node class  
class Node: 
  
# Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null         
          
# Stack class contains a Node object 
class Stack: 
    # Function to initialize head  
    def __init__(self): 
        self.head = None
          
# Function to add an element data in the stack  
    def push(self, data): 
  
        if self.head is None: 
            self.head = Node(data) 
        else: 
            new_node = Node(data) 
            self.head.prev = new_node 
            new_node.next = self.head 
            new_node.prev = None
            self.head = new_node 
              
              
# Function to pop top element and return the element from the stack  
    def pop(self): 
  
        if self.head is None: 
            return None
        else: 
            temp = self.head.data 
            self.head = self.head.next
            self.head.prev = None
            return temp 
  
  
# Function to return top element in the stack  
    def top(self): 
  
        return self.head.data 
  
  
# Function to return the size of the stack  
    def size(self): 
  
        temp = self.head 
        count = 0
        while temp is not None: 
            count = count + 1
            temp = temp.next
        return count 
      
      
# Function to check if the stack is empty or not   
    def isEmpty(self): 
  
        if self.head is None: 
           return True
        else: 
           return False
              
  
# Function to print the stack 
    def printstack(self): 
          
        print("stack elements are:") 
        temp = self.head 
        while temp is not None: 
            print(temp.data, end ="->") 
            temp = temp.next           
          
  
# Code execution starts here          
if __name__=='__main__':  
  
# Start with the empty stack 
  stack = Stack() 
  
# Insert 4 at the beginning. So stack becomes 4->None  
  print("Stack operations using Doubly LinkedList") 
  stack.push(4) 
  
# Insert 5 at the beginning. So stack becomes 4->5->None  
  stack.push(5) 
  
# Insert 6 at the beginning. So stack becomes 4->5->6->None  
  stack.push(6) 
  
# Insert 7 at the beginning. So stack becomes 4->5->6->7->None  
  stack.push(7) 
  
# Print the stack 
  stack.printstack() 
  
# Print the top element 
  print("\nTop element is ", stack.top()) 
  
# Print the stack size 
  print("Size of the stack is ", stack.size()) 
  
# pop the top element 
  stack.pop() 
  
# pop the top element 
  stack.pop() 
    
# two elements are popped 
# Print the stack 
  stack.printstack() 
    
# Print True if the stack is empty else False 
  print("\nstack is empty:", stack.isEmpty()) 

```
#### Output:

```
Stack operations using Doubly LinkedList
stack elements are:
7->6->5->4->
Top element is  7
Size of the stack is  4
stack elements are:
5->4->
stack is empty: False
```


### Queues:

>A Queue is a collection of objects that are inserted and removed using First in First out Principle(FIFO). Insertion is done at the back(Rear) of the Queue and elements are accessed and deleted from first(Front) location in the queue.

### Queue operations:

1. `enqueue()`     : Adds element to the back of Queue.
2. `dequeue()`     : Removes and returns the first element from the queue.
3. `first()`       : Returns the first element of the queue without removing it.
4. `size()`        : returns the number of elements in the Queue.
5. `isEmpty()`     : Return True if Queue is Empty else return False.
6. `printqueue()`  : Print all elements of the Queue.

```python
# A complete working Python program to demonstrate all  
# Queue operations using doubly linked list  
   
# Node class  
class Node: 
   
# Function to initialise the node object 
    def __init__(self, data): 
        self.data = data # Assign data 
        self.next = None # Initialize next as null 
        self.prev = None # Initialize prev as null 
           
           
# Queue class contains a Node object 
class Queue: 
   
    # Function to initialize head  
    def __init__(self): 
        self.head = None
        self.last=None
           
   
# Function to add an element data in the Queue 
    def enqueue(self, data): 
        if self.last is None: 
            self.head =Node(data) 
            self.last =self.head 
        else: 
            self.last.next = Node(data) 
            self.last.next.prev=self.last 
            self.last = self.last.next
               
               
               
# Function to remove first element and return the element from the queue  
    def dequeue(self): 
   
        if self.head is None: 
            return None
        else: 
            temp= self.head.data 
            self.head = self.head.next
            self.head.prev=None
            return temp 
   
   
# Function to return top element in the queue  
    def first(self): 
   
        return self.head.data 
   
   
# Function to return the size of the queue 
    def size(self): 
   
        temp=self.head 
        count=0
        while temp is not None: 
            count=count+1
            temp=temp.next
        return count 
       
       
# Function to check if the queue is empty or not       
    def isEmpty(self): 
   
        if self.head is None: 
            return True
        else: 
            return False
               
   
# Function to print the stack  
    def printqueue(self): 
           
        print("queue elements are:") 
        temp=self.head 
        while temp is not None: 
            print(temp.data,end="->") 
            temp=temp.next
       
           
# Code execution starts here           
if __name__=='__main__':  
   
# Start with the empty queue 
  queue = Queue() 
   
  print("Queue operations using doubly linked list") 
   
# Insert 4 at the end. So queue becomes 4->None   
  queue.enqueue(4) 
   
# Insert 5 at the end. So queue becomes 4->5None   
  queue.enqueue(5) 
   
# Insert 6 at the end. So queue becomes 4->5->6->None   
  queue.enqueue(6) 
   
# Insert 7 at the end. So queue becomes 4->5->6->7->None   
  queue.enqueue(7) 
   
# Print the queue  
  queue.printqueue() 
   
# Print the first element  
  print("\nfirst element is ",queue.first()) 
   
# Print the queue size  
  print("Size of the queue is ",queue.size()) 
   
# remove the first element  
  queue.dequeue() 
   
# remove the first element  
  queue.dequeue() 
   
# first two elements are removed 
# Print the queue  
  print("After applying dequeue() two times") 
  queue.printqueue() 
   
# Print True if queue is empty else False  
  print("\nqueue is empty:",queue.isEmpty()) 
```

#### Output:

```
Queue operations using doubly linked list
queue elements are:
4->5->6->7->
first element is  4
Size of the queue is  4
After applying dequeue() two times
queue elements are:
6->7->
queue is empty: False
```

# Binary Search Trees

<img src="https://i.imgur.com/25ziRZX.png">

>Binary search trees are binary trees that maintain the following invariant:

>For any given node, all values in the left subtree are less than the value at the given node. Conversely, all values in the right subtree are greater than or equal to the value at the given node.

## Terminology:

- **Root:** The topmost node in the tree
- **Child:** A node directly connected to another node when moving away from the top node.
- **Parent:** A node directly connected to another node when moving _towards_ the root node.
- **Siblings:** Nodes that share the same parent are considered siblings.
- **Leaf:** A node that does not have any children of it's own.

