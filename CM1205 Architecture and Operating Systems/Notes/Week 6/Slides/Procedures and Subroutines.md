### What are some Different Program Structures?

***Spaghetti-Code:***
- *Unrestricted use conditional and unconditional jumps*
- *Very hard to understand*
- *Akin to using GOTO in BASIC*

***Structured Programming:***
- *No GOTO's*
- *Only IF, WHILE, FOR...*
- *Plus procedure and function calls*


### Procedures...

#### What is a Procedure?
*A name block of statements that end in a return instruction (RET)*

#### How are Procedures Defined?
*They are defined by using two directives $PROC$ and $ENDP$, which must be assigned a name. When creating a procedure, that is not the main one, to end it with "ret" before ending the procedure.*

![[Pasted image 20240316152653.png]]


*e.g.*
```assembly
;An example of a basic procedure to sum 3 values.
.586
.model flat, stdcall
option casemap :none
.stack 4096
ExitProcess proto,dwExitCode:dword

.DATA
       
.CODE
main proc

	mov	eax,3
	mov	ebx,6
	mov	ecx,9
	call	sumOf3
	
finish:
	invoke ExitProcess,0


sumOf3 	PROC
		add	eax,ebx
		add	eax,ecx
		ret
	sumOf3 	ENDP

main	endp
end main
```

#### How are Procedures Called?
1. *Procedure is called from within different locations in the program.*
2. *At the end of the Procedure, the RET instruction tells the processor how to return to there it was called from.*
3. *Before a Procedure is called it pushes the address of the instruction immediately following the call onto the stack.*
4. *When the RET instruction is reached the processor Pops the address of the next instruction off of the stack.*


#### How do you Pass Parameters into a Procedure?
*First you need to decide how to pass each parameter either by [[Procedures and Subroutines#Value|value]] or [[Procedures and Subroutines#Reference|reference]].*
*Secondly you need to decide where to pass the parameters, in the [[Procedures and Subroutines#Registers|registers]], [[Procedures and Subroutines#Global Variables|global variables]], [[Procedures and Subroutines#Using the Stack|using the stack]], in a parameter block or in the code-stream.*


#### How do you Pass Parameters by:
```assembly;An example of passing parameters by value and passing parameters by reference.
;Watch the changes of num
.586
.MODEL FLAT,stdcall
.STACK 4096
extrn ExitProcess@4: proc

.DATA
	num DD 12345678H
.CODE
main proc

	mov ebx, 0

	mov eax, num
	call PassByValue

	lea eax, num ; The lea (load effective address) instruction is used to put a memory address into the destination.
	call PassByReference

	
finish:
	push 0
	call ExitProcess@4

PassByValue Proc
	mov eax, ebx
	ret
PassByValue endp


PassByReference Proc 
	mov [eax], ebx
	ret
PassByReference endp 


main	endp
end main
```
##### Value:
*The Procedure receives a copy of the parameter.*

##### Reference:
*The Procedure receives an address of a variable.*

- *This must be done by passing the address rather than the value*
- *The called Procedure is given the opportunity to modify the contents of the variables*
- *Only pass by reference if you expect the Procedure to modify the variable*
- *Sometimes this can produce peculiar results, and is less efficient, but is best for passing large data-structures*


#### Where do you Pass Parameters:
##### Registers:
- *Best for a small number of bytes to a Procedure.*
![[Pasted image 20240316154952.png]]

**Python:**
```python
def writeChar(c, reps):
	for counter in range (reps):
		print(c),

writeChar('C',10)
```

```assembly
.586
.model flat, stdcall
option casemap :none
.stack 4096
ExitProcess proto,dwExitCode:dword
; Example of passing parameters to a procedure using registers

.data
	output db 20 dup(?) 
.code 
main	proc
	MOV AL, 'a'		; Parameter - the character to output
	MOV AH, 20		; Parameter - the number of times to output it
	CALL WRITE_CHAR		; Call the procedure

	MOV AL, 'b'		; Parameter - the character to output
	MOV AH, 10		; Parameter - the number of times to output it
	CALL WRITE_CHAR		; Call the procedure
finish:
	invoke ExitProcess,0
main endp

; This is the procedure. It prints out a given character a specified number
; of times. The parameters are:
; 	AL = the character to be output
; 	AH = number of times to output it
WRITE_CHAR proc near
	MOV ECX, 0
	MOV CL, AH		; Set up CX so that we can use LOOP
	MOV DL, AL		; Move the character into DL for DOS output
OUTPUT_CHAR:
	MOV [output+cx],dl	; write DL to output
	LOOP OUTPUT_CHAR	; Repeat until all characters are output
	RET			; Return from the procedure

WRITE_CHAR endp

end main
```

##### Global Variables:
*Best if there are insufficient registers, but is inefficient as it needs to store and retrieve data from the main memory and cannot use on recursion.*

![[Pasted image 20240316155302.png]]

```assembly
.586
.model flat, stdcall
option casemap :none
.stack 4096
ExitProcess proto,dwExitCode:dword
; Example of passing parameters to a procedure using global variables

.data
	output db 20 dup(?) 
	OutChar 	DB ?	; the character to be output
	OutCount 	DB ?	; number of times to output it
.code 
main	proc
	MOV OutChar, 41H	; Parameter - the character to output
	MOV OutCount, 14H	; Parameter - the number of times to output it
	CALL WRITE_CHAR		; Call the procedure

	MOV OutChar, 42H	; Parameter - the character to output
	MOV OutCount, 0AH	; Parameter - the number of times to output it
	CALL WRITE_CHAR		; Call the procedure
finish:
	invoke ExitProcess,0
main endp

; This is the procedure. It prints out a given character a specified number
; of times. The parameters are:
; 	AL = the character to be output
; 	AH = number of times to output it
WRITE_CHAR proc 
	MOV ECX, 0
	MOV CL, [OutCount]		; Set up CX so that we can use LOOP
	MOV DL, [OutChar]		; Move the character into DL for output
OUTPUT_CHAR:
	MOV [output+cx],dl		;  write DL to output
	LOOP OUTPUT_CHAR		; Repeat until all characters are output
	RET						; Return from the procedure
WRITE_CHAR endp
end main
```

##### Using the Stack:

![[Pasted image 20240316155519.png]]

*Push the parameter for the Procedure onto the stack, then the Procedure can:*
- *Pop them from the stack, or*
- *Access them directly through the stack pointer, the Procedure needs to remove them before exiting*
*This is the best general-purpose method for passing parameters, this is best done through an index register where you:*
- *Save the old value of the register on the stack*
- *Set it equal to the top of the stack*
- *We can now access parameters using fixed offsets from the top of the stack*
**Really food for Indexed Addressing**

```assembly
; Example of passing parameters to a procedure using the stack
; X and Y are 12 and 24 respectively, pass these values via stack to a procedure
;which evaluates 3 * x+7*y
.586
.model flat, stdcall
option casemap :none
.stack 4096
ExitProcess proto,dwExitCode:dword

.data
	X DW 12
	Y DW 24

.code
main proc
	push Y
	push X
	call evalProc
finish:
	invoke ExitProcess,0

main endp

; This is the procedure. It prints out a given character a specified number
; of times. The parameters are

evalProc proc 
	PUSH 	EBP			; Setup base pointer (BP) to access parameters
	MOV  	EBP, ESP			;establish a stack frame
	PUSH 	EBX			;save EBX

	MOV	EAX,[EBP+8]		;X VALUE
	IMUL	EAX,3			;3*X
	MOV 	EBX,[EBP+10]		;Y VALUE
	IMUL	EBX,7			;7*Y
	ADD	EAX,EBX			;3*X + 7*Y
	POP	EBX
	POP	EBP
	RET

evalProc endp
end main
```

### How can we Save the State of the Machine?

![[Pasted image 20240316160006.png]]
![[Pasted image 20240316160602.png]]


#### How can we Save the Registers?
![[Pasted image 20240316160711.png]]


#### How can we Save the Local Variables?

![[Pasted image 20240316160748.png]]


### Returning Values: Functions...

*A function is a Procedure which returns a value, which is very similar to the way as we can pass parameters to it.*

![[Pasted image 20240316160949.png]]


### How can we Push Flags to the Stack?

- *There are times it is necessary to save the state of each flag in the processor's flag register.*
- *This is usually done whenever the processor is interrupted.*
- *Saving the flags and restoring them at a later time, along with the processor registers is a proven technique for resuming program execution after an interrupt.*
- *To make life easy the 80x86 family has an instruction to do this automatically.*
- *This is $PUSHF$ with its counterpart $POPF$.*


### How can we use Recursion in Procedures?

![[Pasted image 20240316161410.png]]

- *It is very useful for expressing algorithms such as Sorting, Trees and Graphs and Mathematical Functions*
- *Recursion only works if we pass parameters using the Stack.*