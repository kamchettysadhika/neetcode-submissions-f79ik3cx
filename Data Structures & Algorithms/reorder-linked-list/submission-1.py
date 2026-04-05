class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       # find the middle point 
       slow,fast = head, head.next 
       while fast and fast.next:
           slow = slow.next
           fast = fast.next.next
       second = slow.next # pivot point 
       prev = slow.next= None 
       # reverse the LL 
      
       while second:
           tmp = second.next 
           second.next = prev 
           prev = second 
           second = tmp 
        
       # merge them 
       first,second = head,prev
       while second:
           tmp1,tmp2 = first.next,second.next 
           first.next = second
           second.next = tmp1
           first,second = tmp1, tmp2