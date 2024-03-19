
### What are Intel's 8086 Microprocessors?

*The 8086 Microprocessors were Intel's first true 16-bit Microprocessors.*

![[Pasted image 20240223140711.png]]

*Above are the different registers Intel's 8086 Microprocessor used, but...*

#### What is the Difference between the Segment Registers, the Index Registers and the Status and Control Registers?

***Segment Registers***:
*These are used as a base location for program instructions, data or the stack.*

*e.g.*
- ***CS - Code Segment**, is the base location of program code.*
- ***DS - Data Segment**, is the base Location for Variables.*
- ***SS - Stack Segment**, is the base location of the stack.*
- ***ES - Extra Segment**, is additional base locations for variables in memory.*

***Index Registers***:
*These contain Offsets from a segment register for information we are interested about.*

*e.g.*
- ***BP - Base Pointer**, is the offset from the **SS** register to locate variables on the stack .*
- ***SP - Stack Pointer**, is the offset from the **SS** register to the location of the top of the stack.*
- ***SI - Source Index**, is used for copying strings from various segment registers.*
- ***DI - Destination Index**, is used for the destination for copying strings.*


***Status and Control Registers***:

*e.g.*
- ***IP - Instruction Pointer**, (for example the program counter), is the offset from the **CS** for the next instruction to execute.*
- ***Flags**, are used to contain status flags.*


### What is the Intel Pentium's [[Instruction Set Architecture]]?

*Intel Pentium uses IA-32, which is Intel's 32-bit architecture.*

*There are three main Operating Modes:*
- ***Real Mode**, which acts like an 8088 (program crash = crash)*
- ***Virtual 8086 Mode**, Where the Operating System is informed on the Program Crash.*
- ***Protected Mode**, which is a Full 32-bit machine.*

*There are Four Privilege Levels:*
- ***Level 0**, is the **Kernel** Mode.*
- ***Level 3**, User Mode*
*Level 1 and 2 are Rarely used and Not needed to know.*

*There are $2^{16}$ Segments, each with $2^{32}-1$ addresses, where Windows and Linux only use one segment.

![[Pasted image 20240223142318.png]]
