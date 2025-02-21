# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # left = ListNode()
        # right = ListNode()

        # lh = left
        # rh = right 

        # dummy = ListNode()
        # dummy.next = head 

        # curr = head 
        # i = 0  

        # n = 0
        # while curr:
        #     curr = curr.next 
        #     n += 1

        # prev = None
        # while i < n - k and curr.next:
        #     j = i
        #     tail = curr

        #     while i - j < k and curr.next:
        #         curr.next = prev 
        #         prev = curr

        #         curr = curr.next    
                
        #         i += 1
            
        #     tail.next = curr.next 

        # return dummy.next 

        arr = []

        curr = head 
        while curr:
            arr.append(curr.val)
            curr = curr.next

        i = 0
        ans = []
        while i <= len(arr) - k:
            ans.extend(arr[i:i+k][::-1])
            i += k
        ans.extend(arr[i:])

        # print(ans)

        head = ListNode(ans[0])
        curr = head 

        for i in range(1, len(ans)):
            curr.next = ListNode(ans[i])
            curr = curr.next
        
        return head 
