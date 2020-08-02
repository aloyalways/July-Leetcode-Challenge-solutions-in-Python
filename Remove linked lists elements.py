# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        while head.val==val:
            head=head.next
            if head is None:
                return None
        temp=head
        while temp.next is not None:
            while temp.next.val==val:
                temp.next=temp.next.next
                if temp.next is None:
                    return head
            temp=temp.next
        return head
