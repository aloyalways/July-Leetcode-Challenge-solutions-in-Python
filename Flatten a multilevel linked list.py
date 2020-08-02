"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        curr=head
        stack=[]
        while curr!=None:
            if curr.child!=None:
                curr.child.prev=curr
                if curr.next!=None:
                    curr.next.prev=None
                    stack.append(curr.next)
                curr.next=curr.child
                curr.child=None
            curr=curr.next
        while stack:
            newNode=stack.pop()
            curr.next=newNode
            newNode.prev=curr
            while curr.next!=None:
                curr=curr.next
        return head
