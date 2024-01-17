
##### What is a Set?
*A formal way of dealing with collections of things, e.g. names, numbers etc*

> [!Definition]
> A set is an unordered collection of distinguishable objects which we can decide whether they belong to a set or not.

**e.g.**
![[Pasted image 20231106140909.png]]


##### What is an Element?
*The name to refer to an object within a set, also called "Members as well"*

**The Notation of an Element:**
- The notation x ∈ S, means "x is a element of S"
- The notation x ∉ S, means "x is not an element of S"


##### What is Cardinality?
*The Cardinality is the number of elements a set contains, like ```len()```*


##### What are some Special Sets?
- ℕ, is the set of natural numbers *(All positive integers incl 0)*

- ℤ, is the set of integers

- ℚ, is the set of rational numbers *(Those numbers which can be represented as p/q, where p, q ∈ ℤ)*
	- ℚ = {𝑥 ∈ ℝ ∶ 𝑥 = 𝑝𝑞 such that 𝑝, 𝑞 ∈ ℤ}

- ℝ, is the set of real numbers *(All decimal numbers incl 𝜋)*

- ℂ, is the set of complex numbers *(sqrt(−1) but we do not cover this)*


##### How can you Describe Sets Mathematically?

- List the elements: {0, 1, 2, 3, 4, 5}
- This then can be abbreviated as {0, 1, 2, ..., 5}

- Describe the elements in terms of some properties they satisfy:
	- {x:x is an integer and 0 ≤ x < 10}

- Describe the elements as the set of all elements in some other set they satisfy some properties:
	- {x ∈ ℤ: 0 ≤ x < 10}


##### What are the Different types of Subsets?

- **Subset:**
	- *A is a **Subset** of B (𝐴 ⊆ 𝐵) if every element in A is also an element of B*
- **Equality:**
	- *A is **Equal** to B (A = B) if they have exactly the same elements.*
- **Proper Subset:**
	- *A is a **Proper Subset** of B (𝐴 ⊂ 𝐵) if it is a Subset of B but not equal to B*
	- *i.e. 𝐴 ⊆ 𝐵 and 𝐴 ≠ 𝐵*


##### How are Empty and Universal Sets Defined?

- *Empty Sets are Sets with zero elements, and are denoted by {} or ∅*
- *Universal sets are sets with all the possible elements, denoted by 𝕌, and the definition of 𝕌 changes on the context*


##### What is a Finite set and an Infinite set?

- *A set is finite if either S = ∅ or there is a Bijection, falls in the Bijective function category (found in [[Functions]])*
- *A set is infinite if it is not finite*


##### What are Countable and Incountable sets?

- *A set S is countable if it is either finite or has the same cardinality as ℕ*
- *A set S is incountable if it is not countable, thus has a cardinality of | S | > ℕ*


##### What are some Operations on Sets?

- **Union:**
	- *The union of sets A and B is denoted by A ∪ B, and is defined by {x: x ∈ 𝐴 or x ∈ 𝐵}*
	- *What is in both sets put together*
- **Intersection:**
	- *The intersection of sets A and B is denoted by A ∩ B, and is defined as { x:x ∈ 𝐴 and x ∈ 𝐵}*
	- *What is the same in both sets*
- **Difference:**
	- *The difference of sets A and B is denoted by A - B, and is defined as {x: x ∈ 𝐴 and x ∉ 𝐵}*
	- *What is the different between the sets*
- **Complement:**
	- *The complement of a set A is denoted by Ā (or A<sup>c</sup>), and is defined as 𝕌 - A or {x: x ∈ 𝕌 and x ∉ A}*
	- *What is left in the 𝕌 if we take out this set*


##### What are some Set Properties?

![[Pasted image 20231108170238.png]]
*This is the same as [[Logic]]*


##### How do Sets work in Python?

- *They can be created by using the ```set()``` function:*
	- ```T = set([2,4,6,8,10,12,14,16,18,20])```

- *Given element a and set A in Python:*
	- To test whether 𝑎 ∈ 𝐴, use ```a in A```
	- To test whether 𝑎 ∉ 𝐴, use ```a not in A```

- Given sets A and B in Python:
	- To test whether 𝐴 ⊆ 𝐵, us ```A <= B```
	- To test whether 𝐴 = 𝐵, use ```A == B```
	- To test whether 𝐴 ⊂ 𝐵, use ```A < B```
	- To test whether A ∪ B, use ```A | B```
	- To test whether A ∩ B, use ```A & B```
	- To test whether A - B, use ```A - B```


##### What is a [[Venn diagrams]]?
*A [[Venn diagrams]] is a diagram which can represent two or more sets relationship*


##### What is a [[Power Set]]?
*A [[Power Set]] is a set which holds all the ways of rearranging the original set with 0 - |sets length| length*


##### What is a [[Partition]]?
*A [[Partition]] is a set which contains different subsets of the original set which all, when using union on the subsets, equal the original set*


##### What is the [[Inclusive-Exclusive Principle]]?
*The [[Inclusive-Exclusive Principle]] is a method of calculating the number of elements in two or more sets, which have used union on them, using their intersections and original lengths*


##### What is the [[Cartesian Product]]?
*The [[Cartesian Product]] is a way of finding all the products of two or more sets in the form of tuples*