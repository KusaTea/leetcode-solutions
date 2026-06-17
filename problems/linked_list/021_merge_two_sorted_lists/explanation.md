# Explanation

## Pattern
linked list

## Idea
Check if list1 or list2 have no nodes, return the opposiete list. If the current list1 value is greater than of the list2, replace them with each other. Create new head that will be returned in the end. Start while loop that will work until list1 has the next node or list2 isn't equal to None. If list1 has the next node: if the current value of list1 is smaller or equal to list2 value, move to the next list1 node, else save next node of list1 in a temporary variable, change the next list1 node by the current list2 node, change list2 variable's value by the temporary variable's value. If list1 doesn't have the next node, add whole list2 to the end of list1 and break the loop.

## Complexity
- Time: O(n + m)
- Space: O(1)
