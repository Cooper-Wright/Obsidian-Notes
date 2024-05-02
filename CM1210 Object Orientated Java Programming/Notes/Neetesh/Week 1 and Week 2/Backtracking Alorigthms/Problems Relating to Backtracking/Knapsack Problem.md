### 0/1 Knapsack Problem Reminder

The **0/1 knapsack problem** is a classic optimisation problem. A hiker wishes to take **$n$ items** on a trip where the weight of item $i$ is **$w_i$**, profit **$p_i$**. The items are to be carried in a knapsack whose weight capacity is **M**. When sum of item weights > **$M$**, some items must be left behind. The question is: which items should be taken/left to maximise the total profit **P**?

### 0/1 Knapsack with Backtracking

Let’s try a new setup using profit density again (**$p/w$ ratio**). The items have been ordered by **p/w** and will be selected and tested in that order. The items are as follows:

![[Pasted image 20240311212449.png]]

### The Fractional Knapsack Problem

The **Fractional knapsack problem**: you can take any fraction of an item. The problem, in other words, is to find where 0 ≤ fi ≤ 1. The goal is to maximize $$max \sum^{n}_{i=1} f_i * p_i$$
*Subject to:* $$\sum_{i∈T} f_i * w_i <= W$$
*Where,* $0<=f_i<=1$


### Maximum Bound on Profit with Fractional Knapsack

As a method of checking if a route down the binary selection tree is profitable or not we are going to use a criteria called **maximum bound on profit**. Taking the items as ordered by **p/w**:

![[Pasted image 20240311212920.png]]

Continuing with the same example but this time omitting the first item. So we can discount this route:

![[Pasted image 20240311212953.png]]

### Backtracking vs. Branch-and-Bound

- **Backtracking** is used for solving **Decision Problem**.
- **Branch-and-Bound** is used for solving **Optimisation Problem**.

#### Backtracking

- In backtracking, the **state space tree** is searched until the solution is obtained.
- Backtracking traverses the state space tree by **DFS (Depth First Search)** manner.
- Backtracking involves **feasibility function**.

#### Branch-and-Bound

- Branch-and-Bound traverse the tree in any manner, **DFS or BFS**.
- Branch-and-Bound involves a **bounding function**.