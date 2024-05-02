
### What is a Digital Computer?

- *An electronic machine which solves problems by carrying out a sequence of instructions, these are its **programs** and are usually very simple.*


### What is Computer Level Hierarchy?

![[Pasted image 20240206180752.png]]

- *Through the principle of Abstraction, we can view the machine to be built from a hierarchy of levels, where each level has a specific function and can be seen as a distinct **virtual machine** which execute a set of instructions (including lower levels instructions).*


### Level 0: Digital Logic Level

- *Digital circuits are constructed from logic gates, where each computes a simple function is based on a small number of digital inputs.*
- *Clusters of logic gates are combined to make registers, control circuits and other computational devices.*

### Level 1: Control Level

- *This is the level where a control unit interests the machine instructions, one at a time from the level above, resulting in the instructions being executed.*
- *What is the difference between Hardwired and Microprogrammed control units:*
	- *Hardwired - control signals emanate from blocks of digital logic components, meaning it is fast but difficult to modify.*
	- *Microprogrammed - machine code is implemented directly by the hardware, meaning it is slower but modifiable.*

### Level 2: Machine Level

- *Also known as [[Instruction Set Architecture]] (ISA) Level.*
- *This consists of machine language.*
- *Where an instruction may be carried out in **hardware** control unit (direct execution) or microprogrammed control unit (aka [[Computer Level Hierarchy#Level 1 Control Level|Level 1]]).*

### Level 3: System Software Level

- *This level deals with operation system instructions, and extends the [[Computer Level Hierarchy#Level 2 Machine Level|ISA Level]] with extra functions for:*
	- *Memory Management*
	- *Process Control*
	- *Interprocess Communication*
	- *Multiprogramming*

### Level 4: Assembly Language Level

- *This is just a human-readable form of one of the underlying languages, which reduces the semantic gap between machine language and high-level languages.*
- *Based on [[Computer Level Hierarchy#Level 2 Machine Level|ISA Level]].*
- *Programs in the assembler and needs to be translated into machine language before execution for **One-to-One Translation**, meaning one assembly instruction translates to one machine instruction.*

### Level 5: High-Level Language Level

- *This level consists of High Level languages such as Java, C languages, python etc, where these languages must be translated to machine language.*

### Level 6: User Level

- *Is composed of applications.*

