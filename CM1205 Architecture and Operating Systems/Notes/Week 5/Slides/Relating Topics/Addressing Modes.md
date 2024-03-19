### What are Addressing Modes?

*An **addressing mode** refers to the method used to specify the location of an operand in an instruction*


### What is Immediate Addressing?

*The simplest addressing mode, where the instruction contains data to be used by the instruction rather than the address by the data*

*e.g. "MOV ECX, 1024"*

*You do not need to get data from the memory*
*It is useful for dealing with constraints.*


### What is Direct Addressing?

*The instruction contains the address of the data to be used by the instruction*

*e.g. "MOV EAX, [1234]"*

*You do need to know the desired address at compile-time, which is useful with global variables.*


### What is Register Addressing?

*Like direct addressing, but the data is in a register rather than a memory location.*

*e.g. -*
*"ADD EBX, ECX"*
*MOV EAX, EBX*

*This mode is very common, where RISC machines are specifically designed to operate in this mode, and are very fast.*

*These are frequently combined with other modes*


### What is Register Indirect Addressing?

*The register contains the address of the data to be used.*

*e.g. MOV [EBX], 0*

*Useful for accessing sequential data structures e.g. arrays from this we can use indirect addressing to access all the elements of an array at address A in turn by using a register to hold the current address*


### What is Indexed Addressing?

*Access memory at a constant offset from a memory address stored in a register.*

*"e.g. "Load EAX with the data at the address stored in EBX plus 8 bytes"*
*MOV EAX, [EBX + 8]*

*Useful for accessing record structures which is also used for local variables and arrays, e.g. suppose we have a student record with four numerical fields at address S, where we can access the individual elements using indexed addressing.*


### What is Based-Indexed Addressing?

*The first Register is "Base", where the second Register along with the Offset is "Index."*

*Access memory at a constant offset from a memory address computed by adding two registers*

*e.g. "Load EAX with the data at the memory addressing found by adding the contents of EBX and ECX and adding 4 bytes.", MOV EAX, [EBX + ECX + 4].*

*"Generalised" addressing mode which can set one register or the offset to 0 to get indexed addressing or indirect addressing, which is useful for accessing record structures, arrays, and arrays of records.*


### What is Stack Addressing?

*All operands are taken from the stack, where no addresses are needed for most instructions*

*The instruction only needs to specify the operation to perform, which may also need to specify constants or memory locations in the instruction too*