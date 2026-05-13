# Explanation

## Pattern
Hashmap

## Idea
Target value is a sum of two variables, therefore by knowing one variable we can calculate the value of the second variable. So, we just need to find out is there required value for the second variable in the list and its' index. The best way to figure it out is to use dictionary to save seen values as keys and their indeces as values. This method is way faster than searching value in the list using 'in' construction, but the suggested solution requires extra space.

## Complexity

- Time: O(n)
- Space: O(n^2)