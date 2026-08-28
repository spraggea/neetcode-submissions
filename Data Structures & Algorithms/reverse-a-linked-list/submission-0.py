# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None

        while current:
            temp_next = current.next #temp value for when we update current.next we still have the next pointer when we change prev = current (line13)
            current.next = prev #
            prev = current #shift pointer
            current = temp_next 
        return prev
