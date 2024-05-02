
### Why are we not Learning High-Level Languages?

*Yipeng says "If the apocalypse happens it would be more beneficial if you know how things are built"*

*Also writing in lower level languages is faster for compiling*


### What is Machine Level Programming?

*Program executing in any microprocessor system consists of the FDE, where the D (decoding) stage involves determining what the instruction means for the Processor in binary-coded instructions. The problem with this is that:*

- *It is very primitive, low level*
- *It is very precise, no room for errors*
- *It is very specific, depends on the CPU*
- *It is very detailed, such as using the registers etc*
- *It is [idiosyncratic](https://dictionary.cambridge.org/dictionary/english/idiosyncratic), leaving you to deal with the weird behaviours of the computer system hardware*

*So why do we learn [[Assembly Language#Why do we learn Assembly Language|Assembly Language]] over Machine Code*


### Why do we learn Assembly Language?

*Since Machine code is difficult to write in as it directly binary, it is much easier to know and understand assembly language.*

*"Assembly Language is a Mnemonic of Machine code"*


### What is Assembly Language?

- *A programming language where each statement produces one machine instruction, thus has a one to one relationship with machine code*
- *It is Human-readable code*
- *Symbols are used for specific addresses, which include registers, variables etc*


### What is Wrong with Assembly Language?

1. *It is hard to learn, even harder than high-level languages due to the mnemonic nature.*

2. *Its hard to read and understand, meaning more thought is needed to understand code (so are some high-level languages though)*

![[Pasted image 20240215145443.png]]


3. *It is hard to debug and maintain, due to lack of experience it is hard to maintain and debug due to unknown errors and lack of the familiarity with bugs.*

4. *It is hard to write, but then there are more tools coming to help with these problems*

5. *It takes a long time to write, this is especially true for inexperience programmers. Sometimes projects will use a mix of high-level and assembly language.*

6. *Compliers have eliminated the need for assembly language, these compilers are better at transforming the code into assembly than humans, but assembly programmers are actually able to write code more efficiently*

7. *Machines are fast enough to make it unneeded, but then again assembly will always be quicker.*

8. *Better speed can also come from a better algorithm, but even that has limits on the speed whereas assembly cuts the compiling time and still allows the use of that algorithm.*

9. *Machines have so much memory there is no need to worry about saving it, but space is important as the smaller the program the cheaper the machine that can run it also smaller programs run faster due to less time compiling.*

10. *It is not portable, Assembly code (and high-level languages) cannot be run on all systems due to the difference in compatibility.*


### What's right with Assembly Language?

1. *It is faster than all other programming languages, which can leads to 5 times the speed of other languages (experience and organisation is needed to make this happen).*

2. *It uses less space, leading to about 50% less space used. This is due to compilers generating bulky code.*

3. *It has a higher capability, in high-level languages they abstract certain parts of hardware without using all possible features where as assembly language allows access to all of them.*

4. *The knowledge of what a compiler turns your code into can help you write better programs overall, such as for jobs like writing compilers; building embedded-systems; creating graphics engines and writing device-drivers.*

5. *It leads to a better understanding of code, meaning you could reverse engineer dangerous code such as malware or virus software.*

