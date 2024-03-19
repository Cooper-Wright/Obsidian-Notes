### Why Test?

- _Software is tested_: Imagine building a house. You want to make sure everything is safe and works correctly before you move in, right? Similarly, testing software helps us find mistakes or bugs that might have happened when creating it.
- _Testing involves planned activities conducted systematically_: Think of it like following a recipe step by step to bake a cake. Testing follows specific steps to check if the software works as expected.
- _It ensures that the software meets customer requirements in terms of **functionality**, **performance**, **reliability**, **security**, and **scalability**_: Just like a phone should be able to make calls and send texts, software needs to do what it's supposed to do without crashing, quickly, securely, and be able to handle more users if needed.

![[Pasted image 20240318110435.png]]

### Testing Objectives

- _Identifying errors through known use cases of the software_: Imagine you're playing a video game. Testing helps us find bugs like if the character gets stuck or if the game suddenly crashes.
- _Good test cases have a high probability of finding undiscovered errors_: It's like having a checklist when packing for a trip. Good test cases help us catch mistakes we might have missed.
- _Successful tests are those that achieve this objective_: If the tests find mistakes, it means they're doing their job!

### When, Who, and How to Test?

![[Pasted image 20240318110513.png]]


- _Testing begins when **executable software** is produced_: Once the software is like a fully baked cake, we start checking if everything tastes right!
- _Test case design starts in **requirements engineering** and is updated in subsequent phases_: It's like planning a trip. You decide where to go, how to get there, and what to do along the way.
- _A separate test group may be involved to avoid biases_: It's like having a referee in a game to make sure everything is fair.
- _Different kinds of tests are needed for **complex systems**_: Just like different tools are needed to fix different parts of a car, different tests are needed for complex software.

### Challenges of Testing

- _Testing is psychologically difficult and may be seen as destructive_: Finding mistakes can be tough, but it's like finding a hidden treasure! It helps make things better.
- _Mistaken attitudes can affect testing effectiveness_: It's like assuming you know all the answers before taking a test. Keeping an open mind helps find more bugs.
- - **Exhaustive testing** is not possible*: Imagine trying every possible combination to unlock a door. It's not practical, so we focus on the most important parts.

### Testing Principles

- _Tests should be traceable to **customer requirements**_: It's like checking a shopping list to make sure you've got everything you need.
- _Tests should be planned long before testing begins_: Planning ahead helps us stay organized and find bugs faster.
- _The **Pareto principle** applies to software testing_: It's like focusing on fixing the most critical issues first to make the biggest impact.
- _Testing should progress from "in the small" to "in the large"_: Just like building a LEGO set, we start with small pieces before putting everything together.
- _Testing should ideally be conducted by an independent third party_: It's like having a referee in a game to make sure everything is fair.

### Testing Strategy

- _Various testing models like **V Model**, **Waterfall Model**, **Iterative Model**, and **Agile** are used_: Think of them as different game plans for winning a match.

#### V Model...

![[Pasted image 20240318110555.png]]

![[Pasted image 20240318110613.png]]

#### Waterfall Model...

![[Pasted image 20240318110642.png]]

#### Iterative Model...

![[Pasted image 20240318110708.png]]

#### Agile...

![[Pasted image 20240318110721.png]]

### Generating Test Cases

![[Pasted image 20240318110734.png]]

- _Design tests that are likely to find errors while minimizing resource usage_: It's like trying to find the most efficient way to solve a puzzle.
- _Approaches include _white-box testing_ and _black-box testing__*: It's like using different tools to fix different parts of a bike.

### White-Box Testing

- _Focuses on understanding **internal functionalities** and program control structures_: It's like peeking inside a watch to see how it works.
- _Techniques like **basis path testing** and **cyclomatic complexity analysis** are used_: It's like counting the gears and springs in a watch to understand its complexity.

![[Pasted image 20240318110810.png]]
![[Pasted image 20240318110828.png]]

![[Pasted image 20240318110844.png]]
![[Pasted image 20240318110856.png]]

### Black Box Testing

- _Focuses on **functional requirements** of the software_: It's like testing if the buttons on a remote control work without knowing how they're wired inside.
- _Derives a set of tests that fully exercises all **functional requirements**_: It's like making sure every button on the remote control does what it's supposed to do.


### White Box versus Black Box

![[Pasted image 20240318141709.png]]


### Unit Testing and Integration Testing

- _Unit testing involves testing individual modules, while integration testing ensures modules work together_: It's like checking each ingredient before baking a cake and then making sure they all mix well together.
- _Different approaches like **top-down** and **bottom-up integration testing** are used_: It's like building a LEGO tower from the top or bottom and making sure each piece fits perfectly.

#### Bottom-up Testing

![[Pasted image 20240318141800.png]]

#### Regression Testing

![[Pasted image 20240318141816.png]]

#### Smoke Testing

![[Pasted image 20240318141831.png]]

### Regression Testing and Smoke Testing

- _Regression testing ensures no new errors are introduced after changes_: It's like rechecking your work after making corrections to avoid new mistakes.
- _Smoke testing verifies the stability of the whole program daily throughout development_: It's like making sure your car starts every morning before heading out.

### Object-Oriented Testing

![[Pasted image 20240318141856.png]]
![[Pasted image 20240318141918.png]]

- _Strategies for testing object-oriented software, including unit testing and integration testing, are outlined_: It's like testing if different parts of a car, like the engine and brakes, work together seamlessly.

![[Pasted image 20240318141928.png]]

### Testing Non-functional Attributes

- _Testing for non-functional attributes like **performance**, **security**, **dependability**, and **energy efficiency** is crucial_: It's like checking if a car is not only fast but also safe and reliable.

### Design for Testability

- _Design principles to make software more testable include **operability**, **observability**, and **controllability**_: It's like designing a house with easy-to-reach light switches and windows for better airflow.

### Conclusion

- _Emphasizes the importance of systematic and early testing using appropriate tools and methodologies: It's like proofreading an essay before submitting it to catch any mistakes and make it better.