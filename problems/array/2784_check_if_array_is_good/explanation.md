# Explanation

## Pattern
Hashtable

## Idea
We need to check if every num except last two is unique. The best choice for unique values is set. We need to go thriugh all the array and remove numbers from set. If a number not in set and it's not the last number, False returns. If it's the last number and counder more than 0, counter decreases by 1, otherwise - False returns.

## Complexity
- Time: O(n)
- Space: O(n^2)