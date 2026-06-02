# Explanation

## Pattern
Stack

## Idea
The most complex function is "getMin", because we need to have O(1) time complexity and we need to consider cases when a user removes the stack minimum value. Therefore, we need to have an additional stack with sequence of minimum values. We don't need to store all the values ​​on the stack because only the topmost value can be removed from the stack. Therefore, when adding a new value, we need to push it onto the stack, then compare it with the last minimum value, and push the smaller of the two onto the minimum stack.

## Complexity
- Time: O(1)
- Space: O(n)
