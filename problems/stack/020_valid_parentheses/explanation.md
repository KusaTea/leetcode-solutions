# Explanation

## Pattern
Stack

## Idea
First of all we need to check if the string has even number of characters. Then, we use a dictionary to transfrom back brackets to straight brackets and stack to save last straight bracket. If the current bracket is staright we add it to the stack. If the current bracket is back we check if the stack is not empty and if the last element of the stack is opposite bracket to the current - if the conditions are True we remove the last element from the stack, else return False. 

## Complexity
- Time: O(n)
- Space: O(n)
