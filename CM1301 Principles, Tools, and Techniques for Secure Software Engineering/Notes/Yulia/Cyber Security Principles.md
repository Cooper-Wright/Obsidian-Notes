---
"Creation:": 2024-04-22 10:07
Modified: 2024-04-22 10:07
tags: Cyber Security Principles
---
### Topic: Security principle?
#### Overview: 
*An introduction to security principles*

### Definitions:



#### Subtopic 1 - What is a Security Principle?

*Due to this being a rich topic, there are security recommendations from previous years which are based on past observations. The Security Principles are usually concise and well-worded.*

#### Subtopic 2 - Historical Overview: The Beginning

*In 1975, Jerome Saltzer and Michael Schroeder wrote a paper "The Protection of Information in Computer Systems", where they proposed eight principles of secure system design*

> [!quote]
> useful principles that can guide the design and contribute to an implementation without security flaws

#### Subtopic 3 - Saltzer and Schroeder Principles

1. *Economy of Mechanism*
2. *Fail Safe Defaults*
3. *Complete Mediation*
4. *Open Design*
5. *Separation of Privilege*
6. *Least Privilege*
7. *Least Common Mechanism*
8. *Psychological Acceptability*

*Two added design principles*
9. *Work Factor*
10. *Compromise Recording*

---

### Topic: The Eight Security Principles
#### Overview: 
*Provide a brief overview of the topic*

### Definitions:



#### Subtopic 1 - Economy of Mechanism

> [!quote]
> "Keep the design as simple and small as possible. This well-known principle applies to any aspect of a system, but it deserves emphasis for protection mechanisms for this reason: design and implementation errors that result in unwanted access paths will not be noticed during normal use(since normal use usually does not include attempts to exercise improper access paths). As a result, techniques such as line-by-line inspection of software and physical examination of hardware that implements protection mechanisms are necessary. For such techniques to be successful, a small and simple design is essential."

*Complexity is the worst enemy of security, the more complex you make your system, the less secure it is going to be, because you will have more vulnerabilities and make more mistakes somewhere in the system.*

*Security is a chain; the weakest link breaks it. Simplicity means fewer components and fewer links*

#### Subtopic 2 - Fail Safe Defaults

> [!quote]
> Base access decisions on permission rather than exclusion. This principle...means that the default situation is lack of access, and the protection scheme identifies conditions under which access is permitted. The alternative, in which mechanisms attempt to identify conditions under which access should be refused, presents the wrong psychological base for secure system design. A conservative design must be based on arguments why objects should be accessible, rather than why they should not. ... A design or implementation mistake in a mechanism that gives explicit permission tends to fail by refusing permission, a safe situation, since it will be quickly detected. On the other hand, a design or implementation mistake in a mechanism that explicitly excludes access tends to fail by allowing access, a failure which may go unnoticed in normal use. This principle applies both to the outward appearance of the protection mechanism and to its underlying implementation.

*The default setting should be the safest means a lack of access by default. When allowing a user access you should argue for that reason and not why they should not have access, and access should be based on permission, not exclusion. If an action fails, the system should be as secure as when the action began.*

#### Subtopic 3 - Complete Mediation

> [!quote]
> Every access to every object must be checked for authority. This principle, when systematically applied, is the primary underpinning of the protection system. It forces a system-wide view of access control, which in addition to normal operation includes initialization, recovery, shutdown, and maintenance. It implies that a fool proof method of identifying the source of every request must be devised. It also requires that proposals to gain performance by remembering the result of an authority check be examined sceptically. If a change in authority occurs, such remembered results must be systematically updated.

*Access rights are completely validated every time an access occurs, Systems should not rely in cached or stored access decisions, this reduces the chance of accidental permission violations.*

***Example 1***
*When a UNIX process tries to read a file, the operating system determines if the process is allowed to read the file. If so, the process receives a file descriptor encoding the allowed access. Whenever the process wants to read the file, it presents the file descriptor to the kernel. The kernel then allows the access. If the owner of the file disallows the process permission to read the file after the file descriptor is issued, the kernel still allows access. This scheme violates the principle of complete mediation ,because the second access is not checked. The cached value is used, resulting in the denial of access being ineffective.* 

***Example 2***
*The Directory Name Service (DNS) caches information mapping hostnames into IP addresses. If an attacker is able to "poison" the cache by implanting records associating a bogus IP address with a name, the host will route connections to that host incorrectly.*

#### Subtopic 4 - Open Design

> [!quote]
The design should not be secret. The mechanisms should not depend on the ignorance of potential attackers, but rather on the possession of specific, more easily protected, keys or passwords. This decoupling of protection mechanisms from protection keys permits the mechanisms to be examined by many reviewers without concern that the review may itself compromise the safeguards. In addition, any sceptical user may be allowed to convince himself that the system he is about to use is adequate for hispurpose.9 Finally, it is simply not realistic to attempt to maintain secrecy for any system which receives wide distribution.

*Security through Obscurity or Security by Obscurity means protecting information or system by making the assets or safeguards secret **but** open design is the concept that the opposite is better.*

*This was originally known as **Kerckhoffs's principle**, which states "A cryptosystem should be secure even if everything about the system, except the key, is public knowledge."*

#### Subtopic 5 - Separation of Privilege

> [!quote]
Where feasible, a protection mechanism that requires two keys to unlock it is more robust and flexible than one that allows access to the presenter of only a single key. The relevance of this observation to computer systems was pointed out by R. Needham in 1973. The reason is that, once the mechanism is locked, the two keys can be physically separated and distinct programs, organizations, or individuals made responsible for them. From then on, no single accident, deception, or breach of trust is sufficient to compromise the protected information. This principle is often used in bank safe-deposit boxes. It is also at work in the defence system that fires a nuclear weapon only if two different people both give the correct command. In a computer system, separated keys apply to any situation in which two or more conditions must be met before access should be permitted. For example, systems providing user-extendible protected datatypes usually depend on separation of privilege for their implementation.

*The **Four eyes Principle** is a requirement that two individuals approve some action before it can be taken, and as such Separation of Privilege requires two (or more) actors to operate in a coordinated manner to perform a security-sensitive operation*

***Separation of Privilege = Separation of Duties = Segregation of Duties***

*This breaks up a process into tasks performed by different individuals*

#### Subtopic 6 - Least Privilege

> [!quote]
> Every program and every user of the system should operate using the least set of privileges necessary to complete the job. Primarily, this principle limits the damage that can result from an accident or error. It also reduces the number of potential interactions among privileged programs to the minimum for correct operation, so that unintentional, unwanted, or improper uses of privilege are less likely to occur. Thus, if a question arises related to misuse of a privilege, the number of programs that must be audited is minimized. Put another way, if a mechanism can provide "firewalls," the principle of least privilege provides a rationale for where to install the firewalls. The military security rule of "need-to-know" is an example of this principle.

***Least privilege = Need-to-know***

***Example**: The Linux sudo command allows to only elevate a user’s permission only for a short period of time when they need to perform a highly privileged operation. For day-to-day tasks and activities, less privileged accounts are used. Privileges of an account should be restricted to a small number of actions that that that account need to perform, and root accounts should only be used in a limited number of cases where it is absolutely necessary*

*Make sure you avoid the "Privilege Creep" problem, which is the gradual accumulation of access rights beyond what an individual needs to do their job, where System developers and administrators have a tendency to add more access rights over time, therefore privileges should be reviewed regularly*

#### Subtopic 7 - Least Common Mechanism

> [!quote]
> Minimize the amount of mechanism common to more than one user and depended on by all users. Every shared mechanism (especially one involving shared variables) represents a potential information path between users and must be designed with great care to be sure it does not unintentionally compromise security. Further, any mechanism serving all users must be certified to the satisfaction of every user, a job presumably harder than satisfying only one or a few users. For example, given the choice of implementing a new function as a supervisor procedure shared by all users or as a library procedure that can be handled as though it were the user's own, choose the latter course. Then, if one or a few users are not satisfied with the level of certification of the function, they can provide a substitute or not use it at all. Either way, they can avoid being harmed by a mistake in it.

*The applicability of least common mechanism **is not universal***

*The Principle says that you should avoid sharing components between users, because sharing leads to a single point of failure. However creating more components leads to increased complexity which contradicts the economy of mechanism principle.*

***