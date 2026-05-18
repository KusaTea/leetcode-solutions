# Explanation

## Pattern
Array, hashtable

## Idea
Sudoku matrix has 9 rows, 9 columns and 9 squares. We have to verify that each of theme don't contains repeated numbers, i.e. we need to check if there any number that we have seen already. The easiest solution is to create 3 lists filled by hashtables: rows (9), columns (9) and squares (3, 3) - and got through each index of the matrix adding seen numbers into the hashtables. If there any repeated number, return False.

## Complexity
- Time: O(1)
- Space: O(1?)
