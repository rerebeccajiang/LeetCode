# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode()
        curr = prehead
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr=curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr=curr.next
            
        
        if l1 is None:
            curr.next = l2
        else:
            curr.next = l1
        
        return prehead.next