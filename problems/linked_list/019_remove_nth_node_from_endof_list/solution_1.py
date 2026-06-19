from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def helper(cur_node, counter):
            if cur_node.next:
                length = helper(cur_node.next, counter + 1)
                if length - n == counter:
                    cur_node.next = cur_node.next.next
                return length

            else:
                return counter
        
        length = helper(head, 1)
        if length == n:
            head = head.next
        return head