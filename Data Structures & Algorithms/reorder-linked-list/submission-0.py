# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        fast= head 
        slow= head
        while fast and fast.next:
            fast= fast.next.next
            slow= slow.next
        mid = slow

        # reverse the last list :
        prev=None
        curr=mid
        while curr:
            curr.next , curr ,prev = prev , curr.next , curr 

        # merge them
        first=head 
        second=prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next

        


        