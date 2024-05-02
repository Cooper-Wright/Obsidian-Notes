### N-Queens Problem

The **n-queens problem** is a classical search problem which requires you to place _n queens_ on an _n x n chessboard_, so that no two queens can attack each other. No two queens may be in the same row, column, or diagonal.

#### State Space Tree Construction for 4-Queens

###### [State Space Tree](https://www.baeldung.com/cs/state-space-search)

For n-queens on n x n chessboard, we can immediately simplify matters by realising that no 2 queens can be in the same row. We start at level-0 in the tree: the root. We create the candidate solutions by constructing a tree (called state space tree) in which the column choices for the 1st queen (the queen in row 1) are stored in level-1 nodes in the tree, the column choices for the 2nd queen (the queen in row 2) are stored in level-2 nodes in the tree, and so on. A path from the root to a leaf is a candidate solution. In total, there are 4_4_4*4= 256 candidate solutions.

#### Backtracking Solution

We use pre-order tree traversal: depth-first search. We visit a child (left first) of root at (1, 1). We check if placing a queen at (1, 1) is promising, as it is the 1st queen placed on the chessboard, so it is promising. We visit the child of (1, 1) at (2, 1), check if placing a queen at (2, 1) is promising. It is non-promising as it is in the same column of the 1st queen, so go back (backtrack) to (1, 1). We visit the next unvisited child of (1, 1) at (2, 2), check if placing a queen at (2, 2) is promising. It is non-promising as it is in the diagonal of the 1st queen, so go back to (1, 1). We repeat the above process until a solution is found or the entire state space tree is traversed.

```
1) Start in the leftmost column  
2) If all queens are placed  
    return true  
3) Try all rows in the current column.  Do following  
   for every tried row.  
    a) If the queen can be placed safely in this row  
       then mark this [row, column] as part of the   
       solution and recursively check if placing    
       queen here leads to a solution.  
    b) If placing queen in [row, column] leads to a  
       solution then return true.  
    c) If placing queen doesn't lead to a solution   
       then unmark this [row, column] (Backtrack)   
       and go to step (a) to try other rows.  
4) If all rows have been tried and nothing worked,   
   return false to trigger backtracking.
```

#### N-Queens Problem: Pseudocode

The detailed pseudo-code to solve this problem would be:

```python(Psuedocode)
queens(index i) # initially called with queens(0)
if promising(i) then
    if i = n then # solution found
        print out col[1] through col[n]
    else
        for j = 1 to n
            col[i+1] = j # set queen in column j
            queens(i+1) # check this position
        end for
    end if
end if
```


#### N-Queens Problem: Python

```python
''' Python3 program to solve N Queen Problem using 
backtracking '''


result = []

# A utility function to print solution


''' A utility function to check if a queen can 
be placed on board[row][col]. Note that this 
function is called when "col" queens are 
already placed in columns from 0 to col -1. 
So we need to check only left side for 
attacking queens '''


def isSafe(board, row, col):

	# Check this row on left side
	for i in range(col):
		if (board[row][i]):
			return False

	# Check upper diagonal on left side
	i = row
	j = col
	while i >= 0 and j >= 0:
		if(board[i][j]):
			return False
		i -= 1
		j -= 1

	# Check lower diagonal on left side
	i = row
	j = col
	while j >= 0 and i < 4:
		if(board[i][j]):
			return False
		i = i + 1
		j = j - 1

	return True


''' A recursive utility function to solve N 
Queen problem '''


def solveNQUtil(board, col):
	''' base case: If all queens are placed 
	then return true '''
	if (col == 4):
		v = []
		for i in board:
		for j in range(len(i)):
			if i[j] == 1:
			v.append(j+1)
		result.append(v)
		return True

	''' Consider this column and try placing 
	this queen in all rows one by one '''
	res = False
	for i in range(4):

		''' Check if queen can be placed on 
		board[i][col] '''
		if (isSafe(board, i, col)):

			# Place this queen in board[i][col]
			board[i][col] = 1

			# Make result true if any placement
			# is possible
			res = solveNQUtil(board, col + 1) or res

			''' If placing queen in board[i][col] 
			doesn't lead to a solution, then 
			remove queen from board[i][col] '''
			board[i][col] = 0 # BACKTRACK

	''' If queen can not be place in any row in 
		this column col then return false '''
	return res


''' This function solves the N Queen problem using 
Backtracking. It mainly uses solveNQUtil() to 
solve the problem. It returns false if queens 
cannot be placed, otherwise return true and 
prints placement of queens in the form of 1s. 
Please note that there may be more than one 
solutions, this function prints one of the 
feasible solutions.'''


def solveNQ(n):
	result.clear()
	board = [[0 for j in range(n)]
			for i in range(n)]
	solveNQUtil(board, 0)
	result.sort()
	return result


# Driver Code
n = 4
res = solveNQ(n)
print(res)

# This code is contributed by YatinGupta

```