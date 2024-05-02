### What is Abstraction...

*“The principle of ignoring those aspects of a subject that are not relevant to the current purpose in order to concentrate solely on those that are. The application of this principle is essential in the development and understanding of all forms of computer system."*


#### What are the Different Abstraction Layers?

1. *The Front-end*
2. *The Back-end, which includes the controller, Business logic and Database Abstraction Layer*
3. *The Database*


### What is the Difference between Information Hiding and Encapsulation?

**Information Hiding**: *Hiding the details of an implementation making them inaccessible to other parts of the program ("private" attributes/methods)*

**Encapsulation**: *Enclose related data and functions in the same module (classes)*


### What is an Abstract Data Type...

*“A data type that is defined solely in terms of the operations that apply to objects of the type without commitment as to how the value of such an object is to be represented”*

*Or more simply an Abstract data type is more concerned with what the data type does, its usage*


#### What are some Examples of ADTs?

![[Pasted image 20240319091621.png]]


### Is a List Abstract Data Type?

*Yes as lists in Python may be concrete but actually that is just the implementation of the abstract data type.*

#### List ADT:
- *Has a sequence*
- *Can have elements with the same value*
- *Can usually add an element anywhere*


### What are [[Composition & Inheritance and Polymorphism#What is an Interface?|Java Interfaces]]?

![[Pasted image 20240319091951.png]]


### What are Stacks?

*They are an Abstract Data Type which, unlike a [[Abstract Data Types#What are Queues?|queue]], has the first item in coming out last.*

![[Pasted image 20240319092138.png]]


### What are Queues?

*They are Abstract Data Types which, unlike a [[Abstract Data Types#What are Stacks?|stack]], has the first item in coming out first*

![[Pasted image 20240319092328.png]]

#### What is an Example of a Real Life Queue?

![[Pasted image 20240319092638.png]]


### What is the Implementation of the Queue?

#### What are the Essential Methods?
- *enqueue*
- *dequeue*

#### What are other Typical Queue Methods?
- *peek*
- *isEmpty*
- *isFull*
- *getLength, clear etc*

#### How would you Code a Basic Array in Java?

```java
public void enqueue(Object theElement) {
	queue[front + numElements] = theElement;
	numElements++;
}

public Object peek() {
	return queue[front];
}

public Object dequeue() {
	Object returnedElement = queue[front];
	queue[front] = null;
	front++;
	numElements--;
	return returnedElement;
}
```


#### What happens with a Moving Front in a Basic Array?

![[Pasted image 20240319094632.png]]
![[Pasted image 20240319094639.png]]
![[Pasted image 20240319094656.png]]
![[Pasted image 20240319094704.png]]

*What we could do is Reindex...*


#### What is Reindexing?

![[Pasted image 20240319094751.png]]
![[Pasted image 20240319094805.png]]


### What are Circular Queues?

*A Circular Queue is an extended version of a normal queue where the last element of the queue is connected to the first element of the queue forming a circle.*

![[Pasted image 20240319094830.png]]

#### How is Resizing done in Circular Queues?

- *It is needed to be done less often, as we can reuse empty space at the front of the queue.*
- *But to ensure enqueue/dequeue still work, we do need to reindex when growing the capacity of the queue...*

![[Pasted image 20240319095219.png]]


