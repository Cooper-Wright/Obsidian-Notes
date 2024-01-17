
*A linear search to find a number in a list of numbers:*

```run-python
def LinearSearch(list, key):
	for i, x in enumerate(list):
		if x == key:
			return i
	return ("Key was not found in the list")

print(LinearSearch([1,2,3,4,5], 5)) # This would print the index 4
print(LinearSearch([1,2,3,4,5], 6)) # This would print "Key was not found in the list"
```


*A linear search to find a string with the key, which is a substring/a part of the string, in a list of strings:*

```run-python
def LinearSearch(list, key):
	for i, x in enumerate(list):
		if key in x:
			return i
	return ("Key was not found in the list")

print(LinearSearch(["apple","banana","cauliflower","dragonfruit"], "fruit")) 
# This would print the index 3

print(LinearSearch(["apple","banana","cauliflower","dragonfruit"], "pineapple")) 
# This would print "Key was not found in the list"
```


##### How well does the Linear Search Algorithm Preform?

*Well first off how do we determine performance?*
- *To analyse performance, we can count how many objects are examined by the algorithm, e.g. for the Linear Search Algorithm it is the line of code below*

```python
if key in x:
```

*Secondly how is determining the performance of an algorithm useful?*
- *It would mean we could guarantee how long the algorithm will take and possibly predict how long, also this would rely heavily on whether the search is successful or unsuccessful*


*Lastly how do we use the Expected Value to find the average runtime of the algorithm?*
- *Suppose the key is equally likely to occur as any element is, thus,*
$$P(key <= a[i]) = \frac {1}{n}$$
-* Let $X$ be the number of elements that need to be compared before finding the key, thus the average case is,*
$$E[X]=1.\frac {1}{n}+2.\frac {1}{n}+3.\frac {1}{n}+...+n.\frac {1}{n}$$
$$= \frac {n(n+1)}{2} = \frac {n+1}{2}$$
*Therefore on average in the linear search, the algorithm would search half the list.*

*Then the worst case is that we would need $n$ comparisons, therefore the only guarantee is that it will be <= n comparisons*