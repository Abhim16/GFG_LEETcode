# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         temp = dummy
#         carry = 0
#         while(l1 != None or l2 != None)or carry:
#             summ = 0
#             if l1 != None:
#                 summ+=l1.val
#                 l1 = l1.next
#             if l2 != None:
#                 summ+=l2.val
#                 l2 = l2.next
#             summ+= carry
#             carry = summ //2
#             node = ListNode(summ % 10)
#             temp.next = node
#             temp = temp.next
#         return dummy.next    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while (l1 != None or l2 != None) or carry:
            sum = 0
            if l1 != None:
                sum += l1.val
                l1 = l1.next
            if l2 != None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
            
        