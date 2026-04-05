class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        dummy = ListNode()
        cur = dummy 

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 
            v2 = l2.val if l2 else 0 
            val = v1+v2+carry 
            carry = val//10 
            val = val%10
            cur.next = ListNode(val)
            cur = cur.next 
            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 
        return dummy.next
    


#  dummy = ListNode()
#        cur = dummy 
#        carry = 0 
#        while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0 
#             v2 = l2.val if l2 else 0 
#             val = v1+v2+carry 
#             carry = val//10 
#             val = val%10
#             cur.next = ListNode(val)

#             cur = cur.next 
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None 
#        return dummy.next


#     #    321 
#     #    123 
#     #    so a linkedlist cannot be like 210 
#     #    because then the number would be 021 
#     #    which has a leading zero 
#     #    can there be a linked list like this 000 
    
#     # questions:
#     # 1) can a linkedlist be like this 000 
#     # 2) can they be of idfferent lengths 
    

#     # what we can do is we can go through the linkedlist
#     # and get the first node of each number and add them 
#     # then go to the next node and then if at all teh number > 9 i.e
#     # its a double digit then we are going to divide by 10 keep the number and then get the remainder and add it 
