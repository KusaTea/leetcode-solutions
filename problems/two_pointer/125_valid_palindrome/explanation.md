# Explanation

## Pattern
two pointers

## Idea
We need to transform all letters to lowercase. Then, create two pointers that corresponds to the first and the last indeces of the string. Start a loop with condition where the first pointer must be less tha the second. If symbols under the indeces are not equal, return False. If the loop ends itself, return True.

## Complexity
- Time: O(n)
- Space: O(1)
