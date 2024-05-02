---
"Creation:": 2024-05-01 19:21
Modified: 2024-05-01 19:21
tags: Memory Management
---
### Topic: Memory Allocation
#### Overview: 
*An overview of Memory Allocation*

### Definitions:



#### Subtopic 1 - What is Memory Allocation

*Memory is usually divided into two partitions, one for the resident OS and one for the user processes, where it is common for the OS to occupy low memory*

*There are two types of Memory Allocation for user processes:*
- *Contiguous*
- *Non-contiguous*

![[Pasted image 20240501192404.png]]

---

### Topic: Contiguous Memory Allocation
#### Overview: 
*A dive into the different types of Contiguous Memory Allocation*

### Definitions:



#### Subtopic 1 - What is Contiguous Memory Allocation?

*Each process is contained in a single contiguous section of memory, where to run the process the system has to find enough contiguous memory to accommodate the entire process*

![[Pasted image 20240501192510.png]]

#### Subtopic 2 - What is Fixed-Partition Memory Allocation?

*This is the idea that you should divide memory into partitions of fixed and equal size, where each partition contains at most one process e.g.*

![[Pasted image 20240501192659.png]]

***Advantages:***
*It is simple*

***Disadvantages:***
*The degree of multiprogramming is limited*
*The size of each process is bound*
*It suffers internal fragmentation, which is memory that is internal to a partition but is not being used*


***Logical and Physical Addresses:***
![[Pasted image 20240501193031.png]]

#### Subtopic 3 - What is Variable-Partition Memory Allocation?

*Initially all memory is considered as one large block of available memory, a hole. When a process needs memory, a hole large enough for the process is allocated.*

*A free-memory list is used to track available memory*

***Memory Protection:***
![[Pasted image 20240502134046.png]]

***Placement Strategies:***
![[Pasted image 20240502134147.png]]

***First-fit:***
![[Pasted image 20240502134203.png]]

***Best-fit:***
![[Pasted image 20240502134223.png]]

***Worst-fit:***
![[Pasted image 20240502134255.png]]


***Benefits:***
- *No internal fragmentation, as allocated memory is just as much as the process request*

***Problems:***
- *Has external fragmentation, as available memory space is broken into chunks*

***How to reduce External Fragmentation:***
- *Coalescing - Merge adjacent holes to form a single larger hole*
- *Memory Compaction - Relocate all occupied areas of memory to one end of main memory, thus leaving a single large free memory hole*

***

### Topic: Non-Contiguous Memory Allocation
#### Overview: 
*Provide a brief overview of the topic*

### Definitions:



#### Subtopic 1 - What is Non-Contiguous Memory Allocation?

*A program is divided into blocks or segments that the system may place in nonadjacent slots in the main memory*

![[Pasted image 20240502134950.png]]

#### Subtopic 2 - What is Paging?

*It is a basic method which:*
- *Breaks physical memory into fixed-sized blocks called **frames***
- *Breaks logical memory into fixed-sized blocks called **pages***
*Where the page size is equal to the frame size*

![[Pasted image 20240502135140.png]]

#### Subtopic 3 - How are Memory Addresses Represented in Paging?

![[Pasted image 20240502135235.png]]

*The page or frame size (since they are the same size) is defined by the hardware and is typically a power of two or $2^n$ where, if the size of the logical address space is $2^m$ bytes and the page size is $2^n$:*
- *The high level $m-n$ buts of the logical address are used for the page number.*
- *The remaining $m$ bits are used for page offset*

![[Pasted image 20240502135500.png]]

#### Subtopic 4 - What is the Hardware for Paging?

![[Pasted image 20240502135529.png]]

*e.g.*
![[Pasted image 20240502135545.png]]

#### Subtopic 5 - How is Sharing Accomplished in a Paging System?

![[Pasted image 20240502135619.png]]

#### Subtopic 6 - Why is Fragmentation caused in a Paging System?

*Internal fragmentation is caused in the paging system.*

*e.g.*
*If the page size = 4KB, and a process requesting 5KB of memory, then the system would allocate two page sizes for the 5KB sized process but then there would be 3KB of unused memory*

***