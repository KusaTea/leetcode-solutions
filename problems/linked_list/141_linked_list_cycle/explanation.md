# Explanation

## Pattern
two pointer

## Idea
Create a slow pointer that is equal to head and a fast pointer that is equal to the next node of the head. Start while loop that works until there the fast pointer and it has the next node. If the slow pointer and the fast pointer are the same nodes, return True, else move the slower pointer by one node, the fast pointer by two nodes. After the loop return False.

## Complexity
- Time: O(N)
- Space: O(1)
