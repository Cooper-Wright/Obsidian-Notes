---
"Creation:": 2024-04-29 20:36
Modified: 2024-04-29 20:36
tags: Untitled
---
### Topic: Operating Systems
#### Overview: 
*An Introduction to Operating System*

### Definitions:



#### Subtopic 1 - What is an Operating System?

*It is an operating system that acts as an intermediary between a user of a computer and the computer hardware, and the OS is a resource allocator which manages the CPU, memory and I/O devices and decides between conflicting requests for efficient and fair resource use.*

*OS is a control program which controls the execution of programs to prevent errors and improper use of the computer*

#### Subtopic 2 - What are the Goal of an Operating System?

*Convenience for the users and programmers*
*Efficiency which maximises the utilisation of the machine's resources and no idling*
*Robutness to errors*
*Security*
*Scalability*

---

### Topic: Computer Systems
#### Overview: 
*A brief overview of the 5 main Computer systems*

### Definitions:



#### Subtopic 1 - What are the 5 Main Computer Systems?

- *Batch systems*
- *Multiprogrammed systems*
- *Timesharing systems*
- *Embedded systems*
- *Distributed systems*

#### Subtopic 2 - What are Batch Systems?

*Early computers:*
- *Input devices: card readers and tape drives*
- *Output devices: line printers, tape drives and card punches*
- *No direct integration between users and the computer system*
- *The major task of the OS was transfer the control from one job to the next*

![[Pasted image 20240429205554.png]]

***Characteristics of process execution:***
- *An I/O operation normally takes much more time than a CPU operation*
- *A process does not need to use the CPU while doing I/O therefore each process spends most its time using I/O devices which is wasteful for the CPU.*

#### Subtopic 3 - What are Multiprogrammed Systems?

***Goal:*** *To keep the CPU as busy as possible*

*The OS keeps several jobs in memory simultaneously through the use of ideas such as CPU scheduling. This means the OS picks and begins one of the jobs in memory and if the current job needs to wait for an I/O process the CPU switches to another job.*

*Positive: Good resource utilisation*
*Negative: no user interaction*

![[Pasted image 20240429210028.png]]

#### Subtopic 4 - What are Timesharing Systems?

*This is a logical extension of multiprogramming also known as multitasking, where its original goal was to enable multiple users to interact with the computer system at the same time.*

![[Pasted image 20240429210521.png]]

*This makes is a support interactive process, where the OS switches very quickly between process and where the interactive processes are given higher priority.*

***Goal:*** *Short response time, which leads to the illusion of interactivity*

*The timesharing systems being more complex than the multiprogrammed systems is due to the better CPU scheduling to achieve a shorter response time and also memory management is better at handling questions like "What is Process A tries to access process B's memory?"*

***Most systems today use timesharing***


***Space-multiplexed Sharing:***

*A resource is divided into two or more distinct units, and then the individual parts are allocated to processes.*

![[Pasted image 20240429211347.png]]


***Time-multiplexed Sharing:***

*A process can use the entire resource for a short period of time.*

![[Pasted image 20240429211453.png]]

***Timesharing:***

*Space-multiplexing for memory and time-multiplexing for CPU.*
*Assume that there are $N$ processes, the OS divides the physical memory into $N$ different blocks and allocates a block to each process then a process that is loaded into its block of memory shares the CPU using time-multiplexing sharing.*

#### Subtopic 5 - What are Embedded Systems?

*A computer is embedded into a complex system where the goals of an embedded system is to:*
- *Minimise the amount of memory and CPU cycles*
- *Use as little electrical power as possible*
- *Hard Real-time constraint, which guarantee a minimum response time*

#### Subtopic 6 - What are Distributed Systems?

*In the mid-1990s, network connectivity became an essential component of a computer system:*
- *Where nearly all modern PCs and workstations are capable of running a web browser*
- *OSs such as Windows, Mac OS and UNIX/Linux now include software, such as a TCP/IP stack, that enables a computer to access the Internet*
- *Windows bundled a web browser as part of the OS, in which they got in trouble*


***Client-Server Systems:***
*A client sends requests to perform an action; a server executes the action and sends back results to the client.*

![[Pasted image 20240429221955.png]]


***Peer-to-Peer Systems:***
*In a client-server system, the server could be a bottleneck*
*In a peer-to-peer system, all nodes within the system are considered peers, and each may act as either a client or a server*

![[Pasted image 20240429222110.png]]

***

### Topic: CPU Scheduling
#### Overview: 
*An overview of CPU Scheduling*

### Definitions:



#### Subtopic 1 - What is the CPU-I/O Burst Cycle?

*Process execution consists of a cycle of a CPU execution and I/O wait, when one process does I/O, a scheduler will typically switch the CPU to another process*

![[Pasted image 20240429222403.png]]

#### Subtopic 2 - What are CPU-Bound and I/O-Bound Processes?

*A typical process execution has a larger number of short CPU bursts or a small number of long CPU bursts*
*A CPU-Bound process is a mostly long CPU bursts*
*A I/O Bound process is a mostly short CPU bursts*

#### Subtopic 3 - What is CPU Scheduling?

*Selecting a waiting process from the ready queue and allocating the CPU to it, where it executes frequently and must be fast*

#### Subtopic 4 - What are the Scheduling Criteria?

*Maximise:*
- *CPU utilisation is the percentage of CPU time spent doing work*
- *Throughput is the number of processes completed per time unit*

*Minimise:*
- *Turnaround time is the interval from submission to completion of a process*
- *Waiting time is the time spent waiting in the ready queue*
- *Response time is the time from submission of a request until the first response is produced*

#### Subtopic 5 - What are the Pre-emptive vs Non-pre-emptive Scheduling?

*Pre-emptive Scheduling is the system that can remove the CPU from the running process, but it needs extra hardware and what if the process is in the middle of updating some data.*

*Non-pre-emptive Scheduling is the system assigned a CPU to a process, the system cannot remove that CPU from that process, which is simpler and is up to the process to release the CPU.*

#### Subtopic 6 - What are Scheduling Algorithms?

![[Pasted image 20240429224754.png]]

*The whole purpose of a CPU scheduling algorithm is to find the order to complete the tasks of the CPU in.*

***FIFO:***
*This means that First-In First-Out also known as FCFS (First-come First-served) and is a Non-pre-emptive process.*

***FIFO Example:***
![[Pasted image 20240429225052.png]]
![[Pasted image 20240429225135.png]]![[Pasted image 20240429225140.png]]


***SJF:***
*Shortest-Job-First, is where the CPU is assigned the process that has the smallest next CPU-burt time, depending on this it may be pre-emptive or non-pre-emptive*

***SJF Example:***

![[Pasted image 20240429230729.png]]
![[Pasted image 20240429230736.png]]

***RR:***
*Round-Robin Scheduling is similar to FIFO but without the pre-emptive behaviour, where instead it first process the queue until it exceeds a set time quantum, then runs the next process*

***RR Example:***

![[Pasted image 20240429230908.png]]
![[Pasted image 20240429230914.png]]

***