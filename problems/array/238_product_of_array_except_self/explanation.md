# Explanation

## Pattern
?

## Idea
There are 3 cases:
1. No 0 in the array: we just need to calculate the product of all the array's elements, then create an array where the ith element is the product result divided by the ith number of the initial array.
2. Only one 0 in the array: calculate product without 0, create an array full of 0, put the ptoduct result by the index of 0 of the initial array.
3. More than one 0 numbers: return array full of 0.

## Complexity
- Time: O(2n)
- Space: O(n + 2)
