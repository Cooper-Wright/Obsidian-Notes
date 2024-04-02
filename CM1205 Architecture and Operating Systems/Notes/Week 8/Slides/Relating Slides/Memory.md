
### What is the Memory Hierarchy?

![[Pasted image 20240325145127.png]]

- *The CPU Registers are accessed at full CPU speed*
- *Cache, 32 Kb to several Mb*
- *Main Memory, 256 Mb to 10's of Gb*
- *Disks, the main workhorse of storage*
- *Tapes and Optical disks which are mainly used for backups*

*As you move down the graph the three parameters on the side increase*


### What are the Parameters?

#### Parameter 1: Access Time...

![[Pasted image 20240325145546.png]]

##### What is an Nanosecond?

![[Pasted image 20240325145607.png]]


#### Parameter 2: Capacity...

![[Pasted image 20240325145642.png]]


![[Pasted image 20240325145721.png]]


#### Parameter 3: Bits per pound...

![[Pasted image 20240325145928.png]]


### What are Memory Addresses?

![[Pasted image 20240325150159.png]]


### What is [[Instruction Set Architecture#What is Byte-Swapping?|Byte Ordering]]?


### What happens if the CPU is fast and the Memory is Slow?

*This means after a memory request, the CPU will not get the word for several cycles.*

#### What are the Two Solutions?

- *Continue Execution, but stall CPU if an instruction references the word before it arrives*
- *Require compiler to to fetch words before they are needed*
	- *May need to insert a NOP (no operation) instructions*
	- *Very difficult to write compilers to do this effectively*

#### What is the Root of the Problem?

##### Economics:
- *Memory accessed on a bus is slow*
- *Fast memory is possible, but to run at full speed, it needs to be located on the same chip as the CPU*
	- *This limits how big CPUs can be made and limits on-chip memory*
- *Very expensive*
- *Limits the size of the memory*

*Therefore do we choose a small amount of fast memory or a large amount of slow memory?*


#### How does Cache help Solve this Problem?

![[Pasted image 20240325151345.png]]![[Pasted image 20240325151402.png]]

##### What are the Different Cache Levels?

![[Pasted image 20240325151448.png]]![[Pasted image 20240325151501.png]]![[Pasted image 20240325151508.png]]



