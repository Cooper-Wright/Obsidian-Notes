
### What is a *Jump* in Assembly Language?

*When writing a program, there are moments when we need to make decisions and alter the program’s flow. This typically occurs due to specific conditions, like a flag changing. In simpler terms, we want to “jump” to a different section of code based on certain criteria.*


### What is a Compare (CMP) Instruction?

*This performs an implied subtraction of two operands, where neither of which are actually altered during the process.*

*Where it changes the Overflow, Sign, Zero, Carry, Auxiliary Carry and Parity Flags, according to the value the destination operand would have had if a subtraction had occurred.*

![[Pasted image 20240305190921.png]]

*CMP provides the basis for most conditional logic structures, if you follow CMP with a conditional jump instruction you can create the assembler equivalent of an IF statement.*

### What are Jump Instructions?

*They are Conditions that the loop must fulfil to break free*

#### Conditional Jumps

| **Condition** | **Description**     | **Flag Condition**    |
| ------------- | ------------------- | --------------------- |
| JZ            | Zero                | ZF = 1                |
| JNZ           | Not Zero            | ZF = 0                |
| JA            | Above               | (CF and ZF) = 0       |
| JB            | Below               | CF = 1                |
| JBE           | Above or equal      | CF or ZF = 1          |
| JAE           | Below or equal      | CF = 0                |
| JC            | No Carry            | CF = 0                |
| JNC           | Carry               | CF = 1                |
| JS            | Greater             | SF = 0 and SF = OF    |
| JNS           | Less                | SF ≠ OF               |
| JGE           | Greater or Equal    | SF = OF               |
| JLE           | Less or Equal       | (ZF = 1) or (SF ≠ OF) |
| JO            | Overflow            | OF = 1                |
| JNO           | Not Overflow        | OF = 0                |
| JS            | Sign                | SF = 1                |
| JNS           | No sign             | SF = 0                |
| JP            | Parity Odd          | PF = 0                |
| JE            | Parity Even         | PF = 1                |
| JCXZ          | CX is equal to zero | None                  |

#### Alias for Conditional Jumps (Seven "Survival Kit" Jumps)

| **Jump**                              | **Description** |
| ------------------------------------- | --------------- |
| Jump (no matter what)                 | -               |
| Jump if the result was zero           | JZ              |
| Jump if the result was Not Zero       | JNZ             |
| Jump if the result was above zero     | JA              |
| Jump if the result was Below zero     | JB              |
| Jump if the result Greater than zero  | JBE             |
| Jump if the result was less than zero | JAE             |

![[Pasted image 20240305191902.png]]


### What do If Statements look like in Assembly?

```python
if (a < b):
	X = 1
else:
	X = 2
```

Looks like:

![[Pasted image 20240305192056.png]]


### What does a For Loop look like in Assembly?

```python
for i in range(10):
	x += 1
```

Looks like:

![[Pasted image 20240305192201.png]]


### What is the Loop Instruction?

*Decrement (e)CX and branch to the label if CX is not zero, if CX = 0, then it will repeat 65535 times.*

![[Pasted image 20240305192449.png]]

*In the code above, if (E)CX is not equal to zero then the instruction will decrement and perform a jump to the target address.*

![[Pasted image 20240305193337.png]]


### What are LOOPE/LOOPZ?

*LOOPE: Loop if equal*
*LOOPZ: Loop if zero*

*In addition to decrementing CX, LOOPZ also examines the state of the zero flag. If set and CX not equal to zero LOOPZ will jump to the target. If CX equals zero, or the zero flag gets cleared within the loop, the loop will terminate. LOOPE is an alternate name for this instruction. There is an instruction LOOPNE/LOOPNZ which is the opposite of LOOPE/LOOPZ.*


### What are While Loops?

![[Pasted image 20240305193845.png]]

