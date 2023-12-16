# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        nxt = None
        while current is not None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            
        head = prev
        return head
#         prev_p = None
#         current_p = head
#         next_p = None

#         # Step 2
#         while current_p:
#             next_p = current_p.next
#             current_p.next = prev_p
#             prev_p = current_p
#             current_p = next_p

#         head = prev_p  # Step 3
#         return head
        