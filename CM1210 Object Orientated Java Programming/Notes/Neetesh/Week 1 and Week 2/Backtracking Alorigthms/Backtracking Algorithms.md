
### Backtracking Introduction

![[Pasted image 20240311203403.png]]


- Backtracking is a methodical way of trying out various sequences of decisions until you find one that works.
- It is used when you have to make a series of decisions among various choices where you don’t have enough information to know what to choose.
- Each decision leads to a new set of choices and some sequence of choices (possibly more than one) may be a solution to your problem.
- In backtracking, we check multiple solutions but also find a method by which some can be eliminated without being explicitly examined, by using specific properties of the problem.

### Backtracking Strategy

![[image-removebg-preview (2).png]]

- Backtracking is applied to problems in which the sequence of items is chosen from a set where that sequence satisfies some criterion.
- The choices at each stage can be represented by branching to corresponding nodes of a state tree.
- The backtracking approach then involves a depth-first (or pre-order) search of the state tree for the problem.
- A general recursive outline method, which includes pruning of the state tree where nodes are not promising, is shown below:

#### Terminology

- A tree is composed of nodes.
- There are three kinds of nodes: The root node, Internal nodes, Leaf nodes.
- Backtracking can be thought of as searching a tree for a particular “goal” leaf node.

#### Backtracking Strategy Code

```python
def checkNode(node v):
    if promising(v):
        if there is a solution at v:
            write the solution
        else:
            for each child u of v:
                checkNode(u)
```

- The definition of promising and the solution condition depend upon the problem being solved.

### Backtracking Animation

- The process of backtracking can be visualized as an animation where the algorithm starts at a certain point, explores different paths (dead ends), and finally finds a successful path.


### What are some Different Examples of Problems Solved with Backtracking Algorithms?

- [[N-Queens Problem]]
- [[Knapsack Problem]]
