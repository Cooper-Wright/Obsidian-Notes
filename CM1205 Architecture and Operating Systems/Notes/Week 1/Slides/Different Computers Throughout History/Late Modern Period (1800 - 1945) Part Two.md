
# Half of The Twentieth Century (1900 - 1945)
### The End of Most Analog Computers ("THE DIGITAL UPRISING")

### Is it Possible to Build a General-Purpose Computer?

***Alan Turing** was the first to describe the principle of modern computers in his **1936 Paper, "Computable Number"**. Which stated that some such machine would be capable of preforming any conceivable mathematical computation if it were representable as an algorithm **(Hypothetical Devices - Turing Machines)**.*

*Turing also introduced the notion of a **"Universal Machine"** (now known as a "Universal Turing Machine"), which is a machine that could perform the task of any other machine, or it could compute anything computable by executing a program.*

*Turing machines still are a central object in the study of theory of computation, and means that modern computers are, except to their limited memory, are **Turing-Complete**.*



### What does the word "Digital" meaning within Computing?

*The word "Digital" was first suggested by **George Robert Stibitz**, where he said it,*

> Refers to where a signal, such as voltage, is not used to directly represent a value (as it would in an analogue computer), but to encode it.

*Stibitz then influenced or created the idea that different levels of voltage within a "computer" could represent different numbers, where voltages in the same interval correspond to an individual number. Thus this meant:*
- *That the robustness (error handling) problem of analogue computers was solved, as less levels of voltages, the more robust, thus this is why we use binary in modern computers as it only has two levels.*
- *Easy to implement, suppose you have a switch, the simplest operation is to turn it off and on, thus binary.*
- *etc*


*Now that we have the principle of what makes a general purpose computer and a way of encoding the computer using binary which can represent True or False, with on and off, how do we use True and False to make a fully functioning encodable computer... Well here comes [[Late Modern Period (1800 - 1945) Part One#Boolean Algebra, George Boole...|George Boole]]*



### How could All of this be Linked and Implemented into Hardware?

*In the Late 1930's American Electronics engineer Claude Shannon and Soviet Logician Victor Shestakov were working on one-to-one correspondence (AKA [[Functions#What are the Different types of Functions?|Bijective Functions]]) between the concepts of Boolean Logic, shown by Boole, and certain electrical Circuits, which are referred to as **Logic Gates**. Where they showed that electronic relays and switches can realise the expression of Boolean Algebra.* 

![[Pasted image 20240201162258.png]]



### Better Architecture, Von Neumann Architecture...
*The von Neumann architecture (AKA The Princeton Architecture), is a computer architecture based on a 1945 description by the mathematician and physicist **John von Neumann** and others in the **"First Draft of a [Report on the EDVAC](https://en.wikipedia.org/wiki/First_Draft_of_a_Report_on_the_EDVAC)"***

![[Pasted image 20240201162641.png]]

*The document describes a design architecture for an electronic digital computer with the following components:*
- *Processing unit that contains the arithmetic logic unit and processor registers*
- *Control unit that contains an instruction register and program counter*
- *Memory that stores data and instructions*
- *External mass storage*
- *Input and output mechanisms*


### What does the term "von Neumann architecture" mean now?
*This now refers to any stored-program computer in which **an instruction fetch and a data operation cannot happen at the same time, due to the sharing of a common bus**.*

*The problem due to the common bus is also referred to as the "von Neumann bottleneck" and often limits the performance of the system.*
