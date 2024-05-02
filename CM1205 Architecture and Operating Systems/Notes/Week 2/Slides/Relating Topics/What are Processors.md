
### What is the Typical Layout of Computer?

![[Pasted image 20240206193804.png]]


### What is the Data Path of a von Neumann Machine?

![[Pasted image 20240206193853.png]]


### Where does the Processor begin Executing a Program?

- *Location zero in the memory*
- *ROM (Read-only Memory)*


### When does the FDE Cycle stop?

*When the Computer is turned off, whereas the Operating System enters a Loop  when there is no I/O Data which delays everything.*


### What is the Instruction Set?

*The Operation the hardware recognises and performs.*

*The representation of an instruction is **binary format for hardware and the opcode, operands and results for software**.*


### What are General-Purpose Registers?

*High-speed hardware device that has a fixed size and supports two operations, **STORE** and **FETCH**.*


### What does the Clock do in the Processor?

*A Quartz Clock emits an alternative sequence of 0 and 1 values at a regular rate*

![[Pasted image 20240206194922.png]]

*Where the speed of the clock is measured in Hertz (HZ), which is the number of times per second the clock cycles through 1 and 0.* 


### How does a Faster Clock Rate affect the Instruction Rate?

*The clock rate means that higher performance is achieved, but the FDE cycle does not process at a fixed rate given by the clock as some operations take longer to be performed.*


### How does the Fetch-Execute Cycle (FDE Cycle) Work?

![[Pasted image 20240206195328.png]]


### What is the Multistage Pipelines?

![[Pasted image 20240206195451.png]]

*To enable high speeds parallel hardware units are used in the processor, where each unit performs one step.*

*Whenever the clock ticks, all stages simultaneously pass the instruction to the right and at any time the pipeline contains 5 instructions, meaning one instruction is completed on each clock cycle.*


### How do You Decide which Instruction set to Use?

*It depends on what you need and what you are willing to trade-off, you can trade-off:*
- *Cost of Hardware*
- *Convenience for a Programmer*
- *Engineering Considerations:*
	- *Chip Size*
	- *Power Consumption*
	- *Heat Dissipation*


### What are Complex (CISC) and Reduced Instruction Sets (RISC)?

*A **CISC** processor includes a large set of instructions, many of which perform complex computations, which can be slow.*

*A **RISC** includes a minimum instruction set and aims to gain the highest possible speed from Fixed-size instruction and is designed to complete one instruction in each clock cycle*


### What are Multi-Core Processor?

- *One integrated circuit which has two or more processors, also known as cores*
- *Implements multiprocessing in a single physical package*
- *Uses message-sharing and shared memory inter-corecommunication methods*
- *Has several tens of cores which may require a Network-on-Chip (NoC)*