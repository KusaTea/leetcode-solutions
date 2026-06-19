from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def helper(cur_node, next_node):
            if not next_node:
                return cur_node
            
            cur_node = helper(cur_node, next_node.next)
            if not cur_node:
                return None
            
            if cur_node == next_node or cur_node.next == next_node:
                next_node.next = None
            else:
                next_node.next = cur_node.next
                cur_node.next = next_node
            
            return next_node.next
            
                
        
        helper(head, head.next)
        