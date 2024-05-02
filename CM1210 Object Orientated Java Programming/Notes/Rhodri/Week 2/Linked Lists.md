---
"Creation:": 2024-04-21 14:20
Modified: 2024-04-21 14:20
tags: Linked Lists
---
### Topic: Singly Linked Lists
#### Overview: 
*An overview of singly linked lists and how to create them.*

### Definitions:



#### Subtopic 1 - What is a Linked Lists?

*Linked lists are like normal lists except the placement in memory is in different placements such as below,*

![[Pasted image 20240421142311.png]]

#### Subtopic 2 - What is a Singly Linked Lists?

*Each Node holds the element and a link to the next Node, where the last Node points to "null"*

![[Pasted image 20240421142400.png]]

*An example of this in java is shown below,*

![[Pasted image 20240421142440.png]]

#### Subtopic 3 - How would you Add an Element to the front of the Linked List?

*Create a new Node with "next" set to the existing head of our list, e.g. in the Singly Linked List set "head" to our new Node and increase "size" by one.*

![[Pasted image 20240421142628.png]]

#### Subtopic 4 - How would you Add an Element to the back of the Linked List?

*Create a new Node with "next" set to null, then set the current "tail" Node's to "next" to our new Node*

![[Pasted image 20240421142800.png]]

*For example set the current "tail" Node's "next" reference to our new Node, then set "tail" to now point at our new Node, and increase the size by one*

![[Pasted image 20240421142935.png]]

#### Subtopic 5 - How would you Add an Element in the Middle of the Linked List?

*Adding a new Node in the middle, means you should create a new Node, and point it to the list Node it will precede, then change the previous pointer to point to our new Node*

![[Pasted image 20240421143135.png]]

---

### Topic: Doubly Linked Lists
#### Overview: 
*An overview of doubly linked lists.*

### Definitions:



#### Subtopic 1 - What is a Doubly Linked List?

![[Pasted image 20240421143214.png]]

![[Pasted image 20240421143223.png]]

#### Subtopic 2 - What is Sentinels within a Doubly Linked List?

*There are "dummy" nodes at the start and end of a list, making the inserting and removing easier*

![[Pasted image 20240421143345.png]]

#### Subtopic 3 - How do you Add to the Front of a Doubly Linked list?

![[Pasted image 20240421143623.png]]

![[Pasted image 20240421143647.png]]

***

### Topic: Linked List vs Array-Based Structures
#### Overview: 
*What are the pros versus cons of Linked Lists vs Array-Based Structures.*

### Definitions:



#### Subtopic 1 - Linked Lists vs Array-Based Structures

![[Pasted image 20240421143841.png]]

![[Pasted image 20240421143915.png]]

***

### Topic: The Applications of Linked Lists
#### Overview: 
*A brief overview of the application of Linked Lists*

### Definitions:



#### Subtopic 1 - What are the Applications of Linked Lists?

*They are used in several file systems*
*Stacks and Queues*
*Circular queues (e.g. Schedulers)*

***