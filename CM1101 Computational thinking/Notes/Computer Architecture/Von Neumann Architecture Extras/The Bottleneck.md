###### Why does the Von Neumann bottleneck occur?

Due to the separation of the CPU and the memory in this architecture, programs are treated as data and thus go through the data bus. But when the data bus is busy from all the data and programs needed within the CPU then there is a limited transfer rate between the CPU and main memory.

###### Why has the Von Neumann bottleneck gotten even worse on modern computers?

Since modern CPU's have sped up and memory size has increased there is a need for information at a time so the CPU can preform at an optimal speed therefore the bottleneck has only gotten worse thus leading to a limit on the effectivity on the CPU.

###### What are some possible solutions for the Von Neumann bottleneck?

1. A Cache
	- Where more frequently used data/programs can be stored
	- Although the bigger the cache the further it must be from to the CPU to stop it overheating.

2. Parallel computing:
	- This comes in the form of:
		- One instruction executed on multiple pieces of data
		- Multiple instructions executed on multiple pieces of data