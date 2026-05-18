# Explanation

## Pattern
Hashtable

## Idea
There are three cases: a number is the end of a sequence, a number is the beginning of a sequence, a number connects two sequences. We must create a hashtable, the key of which will be the numbers being checked, and the values ​​will be the length of the sequence. When considering a number, we need to add the lengths of neighboring sequences and add 1. Next, we need to change the values ​​of the numbers that are the beginning and end of the new sequence.

## Complexity
- Time: O(n)
- Space: O(n)
