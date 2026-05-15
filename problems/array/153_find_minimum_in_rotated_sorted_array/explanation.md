# Explanation

## Pattern
Two pointers

## Idea
We have sorted array (even if it's rotated) and we need to find a num - it's standard solution to use two pointers. We have to check if th middle index more or less than the right index: in the first case we have to move the left index to position (middle + 1); case two - move the right index to position (middle). We can't decrease position in the second case by 1, as the num in the middle position can be minimal and we cannot pass it.

## Complexity
- Time: O(log(n))
- Space: O(n + 3)
