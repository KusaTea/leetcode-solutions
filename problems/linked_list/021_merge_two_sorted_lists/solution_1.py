from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        if list1.val > list2.val:
            list1, list2 = list2, list1
        new_head = list1

        while list1.next or list2:
            if list1.next:
                if list1.next.val <= list2.val:
                    list1 = list1.next
                
                else:
                    tmp = list1.next
                    list1.next = list2
                    list2 = tmp
            
            elif list2:
                list1.next = list2
                list2 = None
                break
                
        return new_head
                

        