
### What is Reliability?
- *A dynamic system characteristic which is a function of the number of software failures.*

### What is Software failure?
- *An event where software behaves in an unexpected way either not to specifcation or expectation*

*The reasons for this are:*
- *faults in the program*
- *faulty or incomplete specifications*
- *unanticipated user interaction*
- *problems in the hardware or external environment*


### What is the Difference between Fault, Errors and Failures?

![[Pasted image 20240211141654.png]]


### What are the Different types of Standards for Code Reliability?

- ***Reliability**, the degree to which a system **performs specified functions** under **specified conditions** for a **specified period of time**.*
- ***Maturity**, the degree to which a system meets needs for reliability under **normal operation**.*
- ***Availability**, the degree to which a system is **operational and accessible when required** for use.*
- ***Fault Tolerance**, the degree to which a system **operates as intended** despite the **presence of hardware/software faults**.*
- ***Recoverability**, the degree to which, **in the event of a failure, a system can recover the data** directly affected and **re-establish the desired state of the system**.*


### What are the Different Reliability Metrics?

- ***Availability** measures the likelihood that the system is available for use, e.g. the network is available at least 98% of the time and the server servers at least 98% of request correctly.*
- ***Rate of occurrence of failure** measures the frequency of occurrences with which unexpected behaviour is likely to be observed, e.g. if the **ROCOF** is $2/1000$ then every $1000$ transactions $2$ are **likely** fail.*
- ***Mean time to failure** measures the time between observed failures, e.g. if a system is unchanged it indicates how long the system will remain operational before a failure occurs.*
- ***Mean time between failures** measures the time between failures for a system that can recover.*


### What are Reliability Requirements and Failure Classes?

*Reliability requirements are often expressed informally, qualitatively and in an untestable way, e.g. the system should be as reliable as possible and the software shall not have more than $N$ faults/$1000$ lines*

*Failure classes are used to understand faults:*
- ***Transient**: occurs only with **certain inputs***
- ***Permanent**: occurs with **all inputs***
- ***Recoverable**: The system can **recover without operator intervention**.*
- ***Unrecoverable**: Operator **intervention is needed** to recover the system.*
- ***Non-Corrupting**: Failure **does not corrupt** data*
- ***Corrupting**: Failure **corrupts** data*


### What are the Specifics of Software Reliability?

- *Faults are usually permanent*
- *Reliability depends on the systems usage as: different users require different interactions; users may see a problem that does not appear for others or users may work around a fault or avoid features known to be faulty*
- *Not all failures are equal, e.g. failure in a mission critical aircraft system is worse than multiple failures in a ticket barcode reader.*

![[Pasted image 20240213115506.png]]


![[Pasted image 20240213115616.png]]


### What are some Different Approaches to Software Development?

![[Pasted image 20240213115710.png]]
<sup>Waterfall and Throwaway/Rapid Prototyping/ Evolutionary Prototyping</sup>

![[Pasted image 20240213115813.png]]<sup>Incremental Development and Rational Unified Process</sup>

![[Pasted image 20240213115855.png]]
<sup>Open Source and Agile Software Development</sup>

![[Pasted image 20240213115934.png]]
<sup>XP (eXtreme Programming)</sup>

![[Pasted image 20240213120002.png]]
<sup>Pair Programming</sup>

### How do you Avoid Faults?

- *Use of Iterative design and through testing*
- *Use modular Design*
	- *Develop good structure for the whole program*
	- *Hide information*
	- *Encapsulate functionality*
- *Design algorithm before coding*
	- *Comment, Comment, Comment*
- *Understand common errors (and avoid them)*


### Common Errors:
#### Data Types

![[Pasted image 20240213120803.png]]

#### Loops

![[Pasted image 20240213120909.png]]

#### Conditional Code

![[Pasted image 20240213121025.png]]


### What is Defensive Programming?

- *"Garbage in does not mean Garbage out"* - McConnel (2004)
- *This refers to the fact that the users may input rubbish but the output should never be rubbish, it should detect and handle faults using correction of errors, reporting and failing fast and gracefully (this is called Handling).*


#### What does it mean to Detect Faults within a Program?

- *Check values of all data inputs from users and external systems and devices*
- *Check values of all input parameters to a method or function*
- *Detect errors in calling other modules*
- *Detect environmental errors*
- *Make sure return values are reasonable*

![[Pasted image 20240218150305.png]]


#### What does it mean to Handling exceptions in a Program?

*Mixing normal and error-handling code results in unreadable programs, therefore you should:*
- *Provide dedicated error-channel through the program*
- *Separate normal and error handling code*
- *Group and differentiate error types*

***Definition: An event which occurs during the execution of a program that disrupts the normal flow of the program’s instructions (Oracle 2019)***

![[Pasted image 20240218150251.png]]


### What is Fault Masking?

*To design the system such that faults can be masked and do not need to be detected for example:*
- *Redudancy in time: Repeat computations several times and use majority vote for result.*
- *Redundancy in space: Perform the same operation on different independent copies and use majority vote.*


#### What is N-version programming?

**Development time**:
- *Hand same specification to an odd number of independent development teams*
- *Have all the teams develop software*

**At Run-time**:
- *Run computation on all versions of the software*
- *Use a reliable voting mechanism to select the best software*

**Disadvantages of N-version programming**:
- *Extremely expensive - should mainly be used for very high-risk areas.*
- *Independence is difficult to ensure as there are a lot of same practices and mindsets and common frameworks*


### How can we Model Reliability?

*This means to find a way to assess the reliability of a program using metrics, this should be done before investing time into building the program*

**Different types of Metrics to Measure the Reliability of a piece of Software**:
- *Availability is the probability of a system being operational at a certain point in time, uses the notation $A(t)$.*
- *Mean time to Failure or Mean time between failures*
- *Reliability is the probability of a system being operational from time $0$ to a given time, $t$, with the notation $R(t)$.*

- *Examples of these models*:
	1. *[[Code Reliability#What are Reliability Block Diagrams?|Reliability Block Diagram]]*
	2. *[[Code Reliability#What are Markov Models?|Markov Models]]*


### What are Reliability Block Diagrams?

*The idea for this diagram is to*:
- *Divide the system into blocks*
- *Connect Blocks to achieve functions*
- *Compute the [[Code Reliability#What are the Different Reliability Metrics?|metrics]]*
- *The assumption is that Block failures are independent*

**What are the Different Computations to find the Paths:**

1. *Serial blocks:* $$A(t) = \prod_{i=1}^{n} A_i(t)$$
![[Pasted image 20240218152808.png]]


1. *Parallel blocks*: $$A(t) = 1 - \prod_{i=1}^{n} (1-A_i(t))$$
![[Pasted image 20240218152820.png]]


### What are Markov Models?

*The idea for this diagram is to*:
- *Model System states*
- *Model Temporal Behaviour, which includes the time spent in each state and probability of transition into other states*
- *Compute the [[Code Reliability#What are the Different Reliability Metrics?|metrics]], such as the mean time spent in operational states, mean time until non-operational state is entered and expected costs/performance/profits*

*The method for this diagram is to*:
- *Draw State diagrams*
- *Assign Sojourn (staying in the same place for a temporary time) times*
- *Assign transition Probabilities*
- *Assign initial probabilities*
- *Compute*

*e.g.*
![[Pasted image 20240218153503.png]]
![[Pasted image 20240218153535.png]]
<sup>Siewiorek and Swarz 1992</sup>
![[Pasted image 20240218153639.png]]
<sup>Continuous Time Markov Chain</sup>


