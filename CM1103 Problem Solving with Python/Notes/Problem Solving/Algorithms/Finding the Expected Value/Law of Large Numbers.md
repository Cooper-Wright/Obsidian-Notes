
##### What is the Law of Large Numbers?
*If we repeat an experiment enough times, the mean of our sample results will converge to the expected result, e.g. we can measure through the number of experiments instead of finding an analytic solution*


##### What is the Formula for the Law of Large Numbers?
*Let $X_1,..., X_n$ be a sequence of independent and identically distributed random variables, each having a mean $μ$ and standard deviation $σ$ then,*
$$P(|\frac{X_1,..., X_n}{n} - μ| <  ∈)$$
<sup>for any positive  ∈ approaches 1 as n -> ∞</sup>


##### What is Some Code to Prove this Law of Large Numbers?

```run-python
import random
import matplotlib.pyplot as plt

data = [random.randint(1,6) for i in range(5000)] # Makes a random set of rolls of a dice

means = []
runningtotal = 0

for i, x in enumerate(data):
	runningtotal += x # Is the total number rolled so far
	means.append(runningtotal / (i + 1)) # Adds the mean of the running total to the means list

plt.plot(means, "r-") # Plots the Means list
plt.show() # Shows the Plot
```
