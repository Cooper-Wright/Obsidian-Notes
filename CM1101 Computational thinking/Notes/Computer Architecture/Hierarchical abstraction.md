###### What is abstraction?
*(dictionary)* - "A general term or idea"
*(In CS)* - Separate meaning of implementation e.g. if you go somewhere it implies you will take a plane etc

###### How does this apply to adding?
For adding N numbers:
*What?*
	Input = 1 2 ......
	Output = number

*How?*
	Add all number together or find pairs e.g.
	 N = 100 then you have pairs 100 + 1 = 101 and 50 + 51 = 101 so 101 x 50 = 5050
	
###### How is this done in python?

``` python 
for i in range(n):
	num += 1

print(num)
```

###### How does this "boil down"?
1. Python
2. Assembly Language
3. Machine Code
4. Voltage levels


> [!tip] 
> The Abstraction level, idea of the application, never changes no matter how the code or idea "boils down".

###### What is the program level?
*It deals with the procedure used to carry out the task and are also known as high level programming languages.*


###### What is the instruction level?
*This computer generates a set of machine instructions using a compiler.*

Levels of Instruction levels:
1.  is the Machine code which only the computer can understand, since most people find it impossible to work with 1's and 0's
	- this is more hardware focused such as how the computer responds to the Machine code

2. is Assembly language which is still primitive but understandable

> [!Help] 
> **Hardware changes and so does the machine code does but above implementation level should never change to fit hardware**


###### What is the difference between hardware and software?
*Basically they are the same where software is a more abstract idea of hardware*

[Hierarchical abstraction PDF](https://learningcentral.cf.ac.uk/ultra/courses/_417218_1/outline/file/_7549950_1)
