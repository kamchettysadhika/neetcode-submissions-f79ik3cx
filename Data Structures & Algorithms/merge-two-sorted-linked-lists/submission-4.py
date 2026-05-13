# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = resultList = ListNode() 
    
        while list1 and list2:
        
                if list1.val < list2.val:
                    resultList.next = list1
                    list1 = list1.next
                else:
                    resultList.next = list2
                    list2 = list2.next
                resultList = resultList.next
        resultList.next = list1 or list2
        return dummy.next

                

