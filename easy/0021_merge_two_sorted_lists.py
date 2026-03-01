# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # make dummy
        dummy = ListNode(0)
        current = dummy
        
        # while still hav val on both
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
                
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # 4. Kembalikan jawaban aslinya (buang gerbong pancingan 0)
        return dummy.next
        