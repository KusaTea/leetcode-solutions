# Explanation

## Pattern
Hashmap

## Idea
The easiest way to verify that two strings contains the same characters is to count number of each counter in the first string, than decrease the calculated values if the same character is in the second string. If in the end hashmap is empty, return True, else False.

## Complexity
- Time: O(n)
- Space: O(n^2)
