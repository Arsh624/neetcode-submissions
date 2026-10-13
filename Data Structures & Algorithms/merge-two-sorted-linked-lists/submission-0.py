# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #problem-> 
        #input->
        #edge->
        #ex->
        #approach->
        """
        head1=list1
        head2=list2
        output=ListNode()
        tail=output
        while head1 and head2:
            if head1.val >= head2.val:
                tail.next= head2
                head2=head2.next
            else:
                 tail.next=head1
                 head1=head1.next
            tail=tail.next
        
        if head1:
            tail.next=head1
        elif head2:
            tail.next = head2
        return output.next
            
            

