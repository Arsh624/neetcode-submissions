# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #problem: given head, return head of reversed linked list 
        #input: head
        #edge:
        #example: [0] -> [1] -> [2] -> [3]
                   h 
        #approach:
        """
        curr = head
        prev = None
        while curr:

            #save
            nxt = curr.next
            #flip 
            curr.next= prev 
            # move prev 
            prev = curr
            #move curr
            curr=nxt

        return prev