# Explanation

## Pattern
Stack

## Idea
To understand if one car will catch up another, we need to calculate time that every car need to get to the target point: the first car can catch up the second if the first car is positioned further from the target point than the second and the first car moves faster than the second - otherwise each car will be a separated fleet.
First of all we need to create 2D array by concatenating position and speed arrays. Then, sort the acquired array by position in descending order. Create stack and start a loop for each car: caclualte required time for a car to reach the target point, if it's smaller than the last value in the stack, don't do anything, otherwise, add the calculated time into the stack.
In the end, return the stack's length.

## Complexity
- Time: O(nlogn)
- Space: O(n)
