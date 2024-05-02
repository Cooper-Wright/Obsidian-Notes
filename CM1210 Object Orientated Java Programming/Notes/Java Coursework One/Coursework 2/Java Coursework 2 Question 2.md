*Example Code*

![[Pasted image 20240426121404.png]]

*Report*
My biggest problems for this coursework, was finding the position to add new elements *(also known as the tail pointer)*, making sure that position is correct and making sure that the code does not count $null$ as an $Object$. 

When finding the tail pointer *(since there is no pointer in the class)*, I first tried making a for loop which checked if the item was $null$ from the front pointer when the first $null$ was found it added the object in the position of the first $null$. The only problem with this is that I also needed another for loop in case the front pointer was not at index 0 which lead to a time complexity of $O(n)$, which I knew is not the most efficient I could make it. 

Also another problem which I faced, was that my solution mentioned earlier was incorrectly determining the tail pointer as shown here, *[null, h, d, e, f, g]*, whereas it should be,*[h, null, d, e, f, g]*. After remembering how the wrap around worked on the first Java coursework, by using modulus, I quickly implemented it as shown in the line:

```java
int tail = (this.front + this.numElements) % this.queue.length;,
```

Leading to a more efficient algorithm that would work faster on larger lists *(having a time complexity of $O(1)$ instead of $O(n)$, which is leagues better)*. 

Next up was, when dequeuing an item from the queue the program should not dequeue a $null$ item and count it as a $Object$, thus reducing $numElements$. This lead to a few problems when I was trying to find the tail pointer but my $numElements$ variable was negative, therefore I added an if statement that checked if the value being removed is $null$, if not decrement $numElements$ as shown below.

```java
if (x != null) {
	this.numElements--;
}
```

Overall my enqueue algorithm has a worst time complexity of $O(n)$ when the queue is full and average time complexity of $O(1)$ whereas my dequeue algorithm has a worst and average time complexity of $O(1)$. My algorithm is efficient as can be and works for the supplied example and all others from my individual testing.
