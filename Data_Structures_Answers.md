Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) -> We are setting value at a given index; no searching done

2. What is the space complexity of your ring buffer's `append` function?
O(1) -> We have a predefined space that does not change.

3. What is the runtime complexity of your ring buffer's `get` method?
O(1) -> Predefined size

4. What is the space complexity of your ring buffer's `get` method?
O(1) -> Predefined size


5. What is the runtime complexity of the provided code in `names.py`?
O(n^2) -> Nested for loops; number items could grow indefinitely 

6. What is the space complexity of the provided code in `names.py`?
O(n) -> Space could grow indefinitely

7. What is the runtime complexity of your optimized code in `names.py`?
Using BST
O(n log n) -> Needs to loop through all names[O(n)] and BST loop [O(log n)] of that name

Using set
O(n) -> Looping through duplicate names and appending to duplicates.list

8. What is the space complexity of your optimized code in `names.py`?
Using BST
O(n) -> Indefinite number of duplicates

Using set
O(n) -> Size could grow with duplicates
