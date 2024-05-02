---
"Creation:": 2024-05-01 17:57
Modified: 2024-05-01 17:57
tags:
  - Process
  - Synchronisation
cssclasses: []
---
### Topic: Process Synchronisation
#### Overview: 
*Provide a brief overview of the topic*

### Definitions: 



#### Subtopic 1 - What was the Motivation of Process Synchronisation?

*Data Sharing as this allows cooperating processes through files and messaging, threads that directly share a logical address space and concurrent access to shared data may result in data inconsistency.*

---

### Topic: Critical Section
#### Overview: 
*A look into Critical Sections*

### Definitions:



#### Subtopic 1 - What is the Critical Section of Code?

*Critical section is a segments of code, in which there are shared modifiable data that can be accessed and modified by multiple processes or threads*

*Critical sections can be entered by processes only in a non-overlapping intervals, where two or more processes cannot be in their critical sections*

#### Subtopic 2 - What is the Critical Section Problem?

*The problem is how you regulate access to the critical section, where the solution must be mutually exclusive, have progress and have bounded waiting*

***Mutual exclusion:***
*If one process is executing in its critical section, then no other processes can be executing in their critical section*

***Progress:***
*If no process is executing in its critical section and some processes wish to enter their critical section, then one will be selected to enter its critical section, where the selection cannot be postponed*

***Bounded waiting:***
*There is a bound on the number of times that other processes are allowed to enter their critical sections while a process is waiting, this is to prevent starvation which is when a process or thread is perpetually denied access to some resources it requests*

#### Subtopic 3 - What is the Solution to the Critical Section Problem?

![[Pasted image 20240501183657.png]]

***

### Topic: Semaphore
#### Overview: 
*A introduction to the solution to the Critical section problem, Semaphores...*

### Definitions:



#### Subtopic 1 - What is a Semaphore?

*A Semaphore is a mechanism provided by the system to implement mutual exclusion such that a semaphore is <span style="color:lightblue; font-style:italic;">a special integer variable S that, apart from initialisation, is accessed only through two standard atomic operations "acquire()" and "release()" where it is associated with a queue that stores the references to the process that are waiting.</span>*

***aquire() Operation:***
*This is called when a process wants to enter its critical section, therefore it must be executed indivisibly/atomically*

``` Psuedocode
acquire(S){
	S--;

if (S<0) {
	put this process into the waiting queue	
	and block the process
	}
}
```

***release() Operation:***
*This is called when a process exits its critical section and must also be executed indivisibly/atomically*

```Psudeocode
release(S){
	S++;
	
	if (S<=0) {
		remove a process from the waiting queue and
		wake up the process
	}
}
```

#### Subtopic 2 - How can you use a Semaphore for Mutual Exclusion?

*Mutual exclusion on a semaphore is enforced with the two key operations, acquire() and release()*

![[Pasted image 20240501191022.png]]

#### Subtopic 3 - What is a Mutex Lock and How do we Count Semaphores?

*A Mutex Lock Semaphore is used to control access to the critical section for a process, where its value is ... -3, -2, -1, 0, 1. Where 1 is the highest value of the Mutex Lock Semaphore*

*A Counting Semaphore is used to control access to a given resource consisting a finite number of instances, where its values can range over an unrestricted domain*
#### Subtopic 4 - How do you Initialise a Semaphore?

*Set the Mutex Lock Semaphore to 1, then a Counting Semaphore is initialised to the number og available instances of a given resource*

![[Pasted image 20240501191527.png]]

#### Subtopic 5 - What are the Problems with Semaphores?

*Use of a Semaphore may result in deadlock or starvation situations:*

- *Deadlock is when one or more processes are waiting indefinitely for an event that can only be caused by one of the waiting processes*
- *Starvation is when a process is perpetually denied resource access. Without accessing the resources, the process is unable to complete its task*

#### Subtopic 6 - What are some Examples of Deadlocks?

***Example One:***
![[Pasted image 20240501191941.png]]

***Example Two:***
![[Pasted image 20240501192007.png]]

#### Subtopic 7 - What is an Example of Starvation?

***Example One:***
![[Pasted image 20240501192047.png]]

#### Subtopic 8 - What is an Example of No Mutual Exclusion?

***Example One:***
![[Pasted image 20240501192132.png]]

---