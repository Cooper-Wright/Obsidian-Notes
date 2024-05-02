
### What is the Assembly Language Level?
*The lowest form of human-readable languages which is based on the [[Instruction Set Architecture]] Level, Which to be executed only needs to be translated to machine language before execution.*


### What are Intel 8086 Assembly Languages Instructions?
*This is concentrated on the 32-bit architecture, where most of the instructions involve a [[Intel's Different Types of Microprocessors#What is the Difference between the Segment Registers, the Index Registers and the Status and Control Registers?|Register]] in one form or another.*


### What are the 8086 Registers?

*There are 4 16-bit Registers, $Ax, Bx, Cx, Dx$, which can be split into 8 8-bit Registers:*

- $AH, AL, BH, BL, CH, CL, DH, DL$, *where the $H$ stands for High Byte and the $L$ stands for Low Byte*
- *So for a 16 bit number the 8 most significant bits are stored in $AH$ and the 8 least significant are in $AL$.*


### What are the 8086's General-Purpose Registers?

![[Pasted image 20240223143229.png]]


### What is the Flag Register?

*The flag register is used extensively when controlling the flow of programs*

![[Pasted image 20240223151134.png]]

#### Some Common Flags:

![[Pasted image 20240223151159.png]]
![[Pasted image 20240223151208.png]]

![[Pasted image 20240223151217.png]]


### What is the Basic Structure of an Assembly Language Program?

![[Pasted image 20240223151252.png]]
![[Pasted image 20240223151301.png]]


### Example of Assembly Instructions?

![[Pasted image 20240223151414.png]]
![[Pasted image 20240223151426.png]]


### How does the Assembler know if you are Referencing Hexadecimal, Binary or Decimal?

*The Assembler converts Decimal into Binary but, if you input a number e.g. 26 is this in Hex or Decimal?*

*Therefore we place a capital letter after the number, e.g. 26H = 26 in Hexadecimal, and 26D = 26 in Decimal also 10B = 10 in Binary.*

![[Pasted image 20240223151749.png]]