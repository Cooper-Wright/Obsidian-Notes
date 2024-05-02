
### How to Model a System?

- *[[Use Case Diagrams and Descriptions]] can help with determining key abstractions of system logic*
- *Model information, operations and responsibilities that satisfy the use case/s*


### What is the "Noun Oriented" approach?

1. **Find the Classes**
2. **Find the Attributes**
3. **Find the Operations**


### Step 1: Finding the Classes

*To make a good Use Case you first **underline noun clauses** in **the use-case flow of events**,
then you need to take the classes and **REMOVE**:*

- *Redundant candidates*
- *Vague candidates*
- *Implementation constructs (How it will be Implemented)*
- *Attributes, make sure to save them for later*
- *Operations <u>(An operation implements a service, usually to impact some behaviour)</u>*


*e.g. this*
![[Pasted image 20240131173913.png]]

*Turns to this,*
![[Pasted image 20240131174342.png]]

### Step 2: Finding the Attributes

- *Take the **Attributes** from earlier, or the **nouns** that are: **uniquely owned by an object**; Has **No behaviour** and are **Important**.*

*The example from earlier then becomes this*
![[Pasted image 20240131174751.png]]


**Step 3: Finding the Operations**

- *Operations describe what the classes can do*
- Operations can either be a **command or a question**, only a **command** can change the state of the object, whereas a **question** should never change it
- Use the [[Class-Responsibility-Collaboration Cards (CRC Cards)]] to find operations

*The example from earlier then becomes this*
![[Pasted image 20240131180857.png]]


### Class Diagrams
- *These Class Diagrams can be used as building blocks for visualising components in a system*
- *This way we can model the interaction between components*
- *Therefore Higher level abstraction and leaves implementation details to the developer or development team*


### What are the Different Types of Relationships?

![[Pasted image 20240131181606.png]]



# Associative Relationship

**Navigability:**
- *To describe relationships, we can use labels, which indicate the type of relationship, and directionality, which indicates the path through the relationship*

![[Pasted image 20240131181854.png]]

**Multiplicity:**
- *Classes may be associated with multiple instances of another, therefore we can indicate the degree of association by labelling with a multiplier, as shown below*

![[Pasted image 20240131182009.png]]

*e.g.*
![[Pasted image 20240131182043.png|1000]]



# Aggregate Relationship

- *Aggregate Relationships symbolise ownership and this **ownership can be shared** e.g. you can share a bank account with your spouse, this is good for demonstrating **components of a subsystem**.*


### When Should you use Association or Aggregation?

- *Aggregation implies ownership whereas Association is more relaxed and states the two classes are linked in a loose way. **IF IN DOUBT, GO WITH ASSOCIATION.***



# Composite Relationship

- *Compositions are relationships which **imply strong ownership** of 1 class over one or many others, this is based on a dependence between classes where the **ownee can survive without the owner***


### When Should you use Composition or Aggregation?

- *Aggregation implies ownership, but places **no constraints on how that ownership is implemented***
Whereas,
- *Composition asserts **Sole ownership**, where **when the owner ceases to exist so must the classes it owns***

### When Should you use Composition or Association?

- *We use attributes to **specify the capabilities of a class and what data it store**, if this data itself becomes complex, **we can restructure it into a separate class and use composition***



# Generalising Relationship

- A class may share another's structure and/or behaviour, like how a car relates to a bus they are both vehicle, we can the create a hierarchy of classes which generalises from others.

##### **<u>Those who generalise/inherit are called "subclasses", then these genralise from "superclasses".</u>**

*e.g.*
![[Pasted image 20240131184143.png]]


### Why should we Generalise?

- *It reduces redundancy, e.g. if two or more classes have a lot in common, **then we can refer to these commonalities rather than specifying them each time***
- *It can **reduce complexity in a class**, as its behaviour and structure are inherited*
- ***Reduce, Reuse, Recycle (and Structure!)***



### What is an Example of this?

![[Pasted image 20240131184440.png]]


**Solution One:**
![[Pasted image 20240131184501.png]]


**Solution Two:**
![[Pasted image 20240131184526.png]]


**Solution Three:**
![[Pasted image 20240131184545.png]]


### What is Class Hierarchy?
- *Generalisation is a recursive process*
- *Repeated generalisation allows us to build hierarchical models*
- *Classes at the top of the hierarchy are the most abstract and general*
- *Classes at the bottom are the most specialised*