
##### Think about how to do something!

###### Example:
*How can you, without using the .sqrt() function, can you find the square root of an inputted number*

###### What could we do?
1. Choose a number and see if it is the answer, if not choose another number.
2. Choose a number, x for the number being square rooted, then an accuracy range for how close you want the answer to be to reality, then while the difference between the (guess^2 - x) > A then keep changing the guess to the average of the guess and x/guess. Then keep repeating until you break out the loop.


![[Pasted image 20231005114048.png]]

```python
def SquareRoot():
    y = int(input("Choose a number: "))
    Accuracy = 0.01
    guess = 1

    while abs(guess**2 - y) > Accuracy:
        guess = (guess + (y/guess))/2
    print(guess)

SquareRoot()
```

