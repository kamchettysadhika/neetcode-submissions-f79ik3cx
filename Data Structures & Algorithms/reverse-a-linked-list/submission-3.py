# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr,prev = head,None 
        while curr:
            # store curr.next because we are changing it 
            tmp = curr.next
            # going to update the next to be prev 
            curr.next = prev
            # update our prev to be current through the loop 
            prev = curr
            # update cyrr
            # curr = curr.next but since curr.next is changed we use the temp 
            curr = tmp 
        return prev
