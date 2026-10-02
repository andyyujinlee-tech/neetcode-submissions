# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        reverseList = None # [1] --> [0] --> [0] --> None
        current = head

        while current != None:
            temp = current.next
            current.next = reverseList
            reverseList = current
            current = temp

        return reverseList

        

        

        