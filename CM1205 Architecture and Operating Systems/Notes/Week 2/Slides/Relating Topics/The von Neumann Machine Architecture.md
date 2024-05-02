
### How was the original von Neumann Machine Laid out?

![[Pasted image 20240206183722.png]]


### How is the Modern von Neumann Machine Laid out?

![[Pasted image 20240206184809.png]]

- *The modern version of the "Stored-Program machine Architecture" (von Neumann Architecture) satisfies:*
	- *Three hardware systems: CPU (ALU, Control Unit), Memory System and I/O System.*
	- *Can carry out sequential instruction processing.*
	- *the [[The Bottleneck|von Neumann Bottleneck]].*


### What is the Modified von Neumann Architecture?

![[Pasted image 20240206185913.png]]#

#### What does this Improve Upon?

- *It improves the single data bus to mitigate [[The Bottleneck|the von Neumann Bottleneck]]*
- *It has a data bus which moves data from the main memory to the CPU registers and vice versa*
- *It has the address bus that holds the address of the data that is currently in the data bus.*
- *It has the control bus which carries the necessary control signals that specifies how the information is transferred.*


### What is the Different between The von Neumann Architecture and others?

**Non-von Neumann Architecture:**
- *Most likely not a general-purpose computers.*
- *May not store programs and data in memory, e.g.*
	1. *Neural Network Architecture*
	2. *Cellular automata*
- *May not process a program sequentially and may instead use Parallel processing*

