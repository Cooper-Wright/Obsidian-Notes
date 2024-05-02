---
"Creation:": 2024-05-01 16:57
Modified: 2024-05-01 16:57
tags: Processes and Threads
---
### Topic: Processes
#### Overview: 
*Brief introduction to the idea of processes*

### Definitions:



#### Subtopic 1 - What is a Process?

*A process is a program in execution that contains:*
- *Program code*
- *Data*
	- *Data section such as local and global variables*
	- *Stack or temporary data*
	- *Heap like dynamical memory allocation*
- *The contents of various CPU registers*
- *Data/address/general purpose registers*
- *Special purpose registers*
	- *Program Counter, which indicates what instruction is going to be executed next*
- *State

![[Pasted image 20240501171439.png]]*

#### Subtopic 2 - What are Process States?

*There are usually more processes to be done than CPUs in a system, which means that the CPUs can not ever not be working while having power. Therefore the OS uses an interrupt clock or interval timer to prevent any monopolisation of resources which only allows a process to run for a specific time interval.*

*There are a few process states, which change as a process gets completed:*
- *Running state, the process is being executed on the CPU*
- *Ready state, the process could execute on a CPU when one is available*
- *Blocked (waiting) state, the process is waiting for some event to happen before it can proceed*
- *New (being created) state*
- *Terminated (finished) state*

![[Pasted image 20240501171918.png]]

#### Subtopic 3 - What is a Process Control Block (PCB)?

*Each process is represented by a PCB which usually includes:*
- *Process state*
- *Process ID*
- *The values of the CPU registers*
- *Memory-management information*
- *Scheduling and resource allocation information*

#### Subtopic 4 - What is a Process Queue?

*A Ready queue is a list of the processes that reside in memory and are ready to be executed*
*A Device queue is a list of processes waiting for a particular I/O device*

![[Pasted image 20240501172200.png]]

#### Subtopic 5 - How is the Scheduling of Queues Handled?

![[Pasted image 20240501172323.png]]

#### Subtopic 6 - What is Context Switching?

*Context switching is the process of stopping the current process from executing and beginning the executing of a previously ready process, this requires the CPU to save the execution context of the old process into its PCB and loading it when the context is switched.*

![[Pasted image 20240501172711.png]]
![[Pasted image 20240501172727.png]]

---

### Topic: Threads
#### Overview: 
*Brief introduction to the idea of processes*

### Definitions:



#### Subtopic 1 - What is a Thread?

*All Threads are in the same process where they SHARE:*
- *Memory context e.g. code and data*
- *Other resources*
*And DO NOT SHARE:*
- *Register context*
- *The Threads specific stack*

#### Subtopic 2 - What is the Difference between a Single-Threaded Process and a Multi-Threaded Process?

*Now dont ask me how TF this shit counts as an explanation but this is all he put...*

***Single-Threaded Process:***
![[Pasted image 20240501175408.png]]

***Multi-Threaded Process:***
![[Pasted image 20240501175436.png]]

#### Subtopic 3 - What are the Benefits of Multi-threaded Programming?

1. *Interactivity, like how an application may continue to run even if it is block or is performing a length operation*
2. *Resource sharing, like how threads share the same address space and the resources of the process to which they belong*
3. *Economy, it is faster to create threads and is also faster to context-switch threads*
4. *Increased concurrency in a multiprocessor architectures, as a single-threaded process can only run on one CPU where the threads in multi-threaded process may be running in parallel on different CPUs*

***