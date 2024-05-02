
##### What is a Permutation?
*A permutation of a set of object is an order of the objects in sequence*

*e.g.,*
![[Pasted image 20231120172057.png]]


##### How do you Count Permutations?
*A set B of n objects has n! (= n x (n-1) x (n - 2) x ... x 1) permutations*


##### What are r-Permutations?
*An r-Permutation of a set of n elements is an **ordered selection** of r elements taken from the set without repetition*

*e.g.,*
![[Pasted image 20231120173002.png]]


##### What is the Definition of P(n, r)?
the number of r-Permutations of a set of n elements is given by:
<sup>does not include repetition</sup>
$$p(n,r) = n!/(n-r)!$$


##### How do you do Permutations in Python?

``` python 
import itertools
for perm in itertools.permutations(string_Here):
	print(perm)
```


##### What are r-Combinations?
*An r-Combination of a set of size n is a subset of size r*

*e.g.,*
![[Pasted image 20231120173858.png]]


##### What is the Definition of C(n, r)?
*Let C(n, r) denote the number of r-Combinations of a set of size n, then*

$$C(n,r) = n!/r!(n-r)!$$

![[Pasted image 20231120174317.png]]


##### What is Combinatorial Equivalence?
*Some counting problems can be made easier by recognising when there is a one-to-one correspondence to another problem*

*e.g.,*
![[Pasted image 20231120175312.png]]


##### How do you do r-Combinations in Python?


``` python 
import itertools
for comb in itertools.combinations(list_Here):
	print(comb)
```


##### What does Repetition have to do with Permutations and Combinations?

*Permutations with repetition:*
- *The number of r-permutations of a set of size n is $$n^r$$
- *If repetition is allowed.*


*Combinations with repetitions:*
- *The number of r-combinations of a set of size n is $$C(n+r-1,r)$$
- *If repetition is allowed*

![[Pasted image 20231123123136.png]]

##### What are Some Counting Rules?
- [[The Product Rule]]
- [[The Sum Rule]]


##### What is an Indistinguishable objects?
*Suppose we have $n_1$ objects of type 1, $n_2$ of type 2, $...$, $n_k$ of type k with n = $n_1 +...+ n_k$ .*
*The number of permutations of these objects is:*
$$\frac {n!}{n_1!n_2!...n_k!}$$


##### Why this Formula?

![[Pasted image 20231127133850.png]]