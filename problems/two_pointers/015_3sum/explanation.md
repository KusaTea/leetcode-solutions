# Explanation

## Pattern
tow pointers

## Idea
We need to find 3 numbers that in sum gives us 0. First of all we need to sort a given array. Then, we need to take the first num and check if it's greater than 0, beacuse we can't get 0 in sum if the smallest number is more than 0. Next, check if the current number is equal to the last one. Finally, we create two pointers and move them to each other based on cases:
1. Sum of two last values is smaller than -num1: increase left pointer by 1
2. Sum of two last values is greater than -num1: decrease right pointer by 1
3. Sum of two last values is equal than -num1: add three numbers to the answer list, increase the left pointer by 1 while it's equal to the last number of this pointer, decrease the right pointer by 1 while it's equal to the last number of this pointer.

## Complexity
- Time: O(n^2)
- Space: O(1)
