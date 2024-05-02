***Question A:***

*Monday*
![[Pasted image 20240423122226.png]]

*Tuesday*
![[Pasted image 20240423122254.png]]

*Wednesday*
![[Pasted image 20240423122317.png]]

*Thursday*
![[Pasted image 20240423122332.png]]

*Friday*
![[Pasted image 20240423122350.png]]

*Saturday*
![[Pasted image 20240423122405.png]]

*Sunday*
![[Pasted image 20240423122424.png]]

*Pseudocode*
![[Pasted image 20240425172309.png]]![[Pasted image 20240425172318.png]]

***Question B:***

![[Pasted image 20240423132715.png]]

***Question C:***

![[Pasted image 20240423133128.png]]

![[Pasted image 20240423133155.png]]


***Question D:***
When first thinking about my hybrid sorting algorithm, I used Insertion sort thinking it would be safe to get it working then increase the speed after being secure in the speed of this one. After implementing the insertion sort, I found that the cut off point matters a lot more than I anticipated, therefore I after some testing I found the lowest average time came from lists of 16 or less. After this I felt unsatisfied with my timings being around 20ms less overall than the original quick sort and decided to look for some possible other hybrid algorithms and came across a few, but one that was quite close to my previous one was the ["introspective algorithm"](https://en.wikipedia.org/wiki/Introsort), which is a mixture of my previous hybrid search but includes heapsort which occurs when the maximum recursion depth is too high. As for the time complexity of the first hybrid algorithm has a worst case of $O(n^2)$ whereas the new hybrid algorithm has a worst case of $O(nlog(n))$, also with the algorithm I tried to find other pivots such as the random Median of five method, which although promising did not lead to results that did not hinder the times and increase my overall time by 5-50ms due to the extra calculation. Before my final algorithm I tried using Merge sort with Quick sort but found it took longer for the shorter array lists. After this I tired to find more sorting algorithms and came across the radix search which I saw had a time complexity of $O(n*d)$ (where d is the number of digits in the largest number) but found it took is better with numbers that are smaller whereas we do not have that luxury in this coursework, therefore I did not follow through with these ideas. In the end, my final sorting algorithm combined the strengths of three algorithms and make a more efficient and quicker sorting time.