# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        dummyNode.next = head 

        prev = cur = dummyNode
        for i in range(n):
            cur = cur.next

        while cur.next:
            prev = prev.next
            cur = cur.next
        
        prev.next = prev.next.next

        return dummyNode.next
