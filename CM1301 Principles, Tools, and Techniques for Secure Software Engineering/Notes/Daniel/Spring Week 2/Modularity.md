
### What is Modularity?
- *The decomposition of an object into a set of smaller objects.*
- *Thinking in terms of modules rather than the **whole end product**.*


### What is a Module?
- *A logical unit of a system*
- *Responsible for a small set of tasks the system must fulfil*
- *Hides its internal details (Abstraction)*


### Why should we Use Modularity?
![[Pasted image 20240204205819.png]]


### What's Wrong with the Normal (Monolithic) Method?
![[Pasted image 20240204205905.png]]


### How do we Determine if a Modular Design is Good?

**Cohesion**:
- *The affinity of the module's components*
- *How well is the module put together?*

**Coupling**:
- *The degree to which a module is associated with another*
- *How strong are the inter-module connections*

***We want High Cohesion and Low Coupling!!***

![[Pasted image 20240204210121.png]]
![[Pasted image 20240204210133.png]]


### What is Functional Independence?

*Aiming to maximize cohesion by:*
- *Ensuring a module has a single, well defined purpose*
- *It has one thing to do*
- *It doesn't deal with unrelated functions*

*Aiming to minimize coupling by:*
- Ensuring that dependencies between modules are kept to as few as possible

***These aims sometimes conflict with one another...***


### What are the Advantages of Strong Cohesion and Weak Coupling?
![[Pasted image 20240204210411.png]]


### How can we Engineer in a Modular Fashion?

**Think! in terms of...**
- *Cohesion: describe each module's purpose*
- *Functions: reusable, and operates by sharing data*
- *Object Oriented Programming.*


### What is a Simple Exercise to Check if a Module is Cohesive?
![[Pasted image 20240204210635.png]]


### What are Functions?
![[Pasted image 20240204210746.png]]![[Pasted image 20240204210804.png]]
![[Pasted image 20240204210823.png]]


### What is the Design of Object Oriented?

*There are two parts:*
- ***Objects**, their attributes, their methods and their relationship between objects*
- ***System Functionality**, the passing of messages between a set of objects.*


### What are Classes?
![[Pasted image 20240204211047.png]]
![[Pasted image 20240204211103.png]]


### How is can you be Effective with Your Modular Design?

- *Refinement: Create multiple representations of a system, where the next is more detailed than the last.*
- *Abstraction: Concentrate on essential issues and ignore details that are irrelevant on the current representation*
- *Information Hiding:*
	1. *Hides internal details of processing, data and control activties*
	2. *Communicate only through well-defined interfaces*


### Why should you Bother with Modular Design?
![[Pasted image 20240204211430.png]]