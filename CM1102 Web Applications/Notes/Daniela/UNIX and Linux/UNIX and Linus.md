##### What is History of UNIX?
*The original UNIX was [1970s AT&T Bell Labs](https://en.wikipedia.org/wiki/Bell_Labs)*
*UNIX Clones: AIX, HPUX, SunOS, Xenix*
*UNIX Standards: BSD, System V, Posix*


##### How did UNIX affect the Open Source Movement?
*It helped start the the Open Source Movement and lead to the creation of:*
- *Free Software Foundations (GNU)*
- *Minix (Andy Tanenbaum)*
- *Linux (Linus Torvalds)*



##### Terminals and Terminal Emulators (How the Shell works?):
- *The shell is an interactive environment for executing UNIX commands, and is started up when you log into a terminal or open a terminal window.*
- *The different types of shells are ==sh==, ==tcsh== or ==bash== etc.*
- *The basic idea for the shell is that you input a key in a command then wait for it to complete and then input a key in another command etc*


##### What are some practical UNIX Commands?

![[Pasted image 20231127124203.png]]


```
cp file1 file2 
```
- *This creates a copy of file1 named file2*
- *Where they both have the same contents but have different names and are different files*

```
In file1 file2
```
- *This creates a link of file1 named file2*
- *Where file1 and file2 point to the same file so editing one will affect both*


##### What is the Difference between Hard Links and Symbolic Links?

```
in file1 file2
```
- *This creates a hard link*
- *Both files have the same inode (ls -i)*
- *Works only within the same file system*

```
in -s file1 file2
```
- *This creates a symbolic link*
- *file2 will point to file1, like a shortcut, and creates a problem when file1 is deleted*
- *works within the same or different file system*


##### What are the Users and File Permissions?

*Each file has an owner and group, where the file permissions for reading, writing and/or executing are set for the owner, group and others.*

*where r is to read, w is to write and x is to execute*

![[Pasted image 20240104132251.png]]


*Each directory also has the same permissions except reading is to see the contents, writing is to alter the contents and executing is the ability to enter the directory and access its file.*

![[Pasted image 20240104132449.png]]


##### What are some different Commands to change these Permissions in the Linux terminal?

![[Pasted image 20240104132610.png]]
![[Pasted image 20240104132632.png]]


##### What are Redirected I/O?

*Although the standard input is the keyboard and standard output is the screen, it is possible to redirect the standard inputs and outputs from and to a file*

![[Pasted image 20240104132755.png]]


##### What are Shell Scripts?

*The shell also provides a programming environment*

*e.g.*
```
for i in *.txt; do
	echo $i;
	cat $i;
done
```


*some other key features include:*
![[Pasted image 20240104133018.png]]


##### What are Environment variables?

*These are shell variables with special meanings, some of which include:*

```
$HOME  $SHELL  $TERM  $PATH
```

*These variables are usually set in files like /etc/profile and ~/profile*

*You can also set your own environment variables and can use and view them.*


##### How is the Unix File System Structured?

![[Pasted image 20240104133428.png]]


##### What are Processes?

*They are a program that is currently running, where each process has a PID and a parent, within the user space compared to the kernels running in the kernel space.*


##### How do you Start a Process?

```
cp hugefile1 hugefile2 &
```


##### How do you Stop a Process and Resuming it in the background or Fully Stopping a Process?

*Stopping and Resuming in Background:*
```
cp hugefile1 hugefile2 #stopping it
^Z
bg
```

Stopping Fully (or Killing):
```
kill %1 #or the job number
kill 123 #or any other process number
kill -9 123 # if the process is not listening (force stop)
```

