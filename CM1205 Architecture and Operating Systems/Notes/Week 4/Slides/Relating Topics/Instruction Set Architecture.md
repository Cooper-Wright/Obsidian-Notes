
### What is Instruction Set Architecture (ISA)?
*This is an overview of the **Intel 8086 and Pentium Processor** ISA.*.

- *It is the Interface between software and hardware, where programs are translated into ISA-level "machine code" instructions. In which hardware executes these directly.*
- A good ISA should be:
	- *Easy to implement in hardware, making it simple, future-proof and cost effective*
	- *Easy to compile programs for, meaning it should be regular and flexible.*


### What are the Properties of an ISA?

1. **Static Properties**:
	- *[[Memory model]], register layout, data-types, instruction set, execution modes*

2. **Dynamic Properties**:
	- *Instruction performance and semantics*

3. **Sometimes formally defined**
4. **Sometimes deliberately obscured (or protected)**


### What is the Difference between the Intel line of microprocessors and those made by other Manufacturers?

*Intel has a unique method of storing numbers in memory, known as [[Instruction Set Architecture#What is Byte-Swapping?|Byte Swapping]].*


### What is Byte-Swapping?

*This is a technique where when a number larger than 1 byte (or 8 bits) is written into the system's memory, the **low byte is written into the first memory slot and the high byte into the second memory location**.*

*Also known as **little endian/big endian**.*

#### What is Big Endian?

- *Usually a MainFrame based systems and Motorola **(Most Non-Intel Systems)***
- *Big-end is stored first (e.g. the most significant byte is stored at the lowest address)*

*e.g.*
![[Pasted image 20240223135423.png]]


#### What is Little Endian?

- ***Intel-Based systems** AKA Byte Swap*
- *Low-end is stored first (e.g. the most significant byte is stored at the highest address)*

*e.g.*
![[Pasted image 20240223135544.png]]

*For Little Endian, Programmers must remember to use the proper practice of byte-swapping or realise that they're programs do not work.*