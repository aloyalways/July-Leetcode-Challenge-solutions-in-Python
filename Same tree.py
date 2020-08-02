# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool: 
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        
        queue=[]
        tree1=[]
        queue.append(p)
        while len(queue)>0:
            if queue[0] is "Null":
                tree1.append(None)
                queue.pop(0)
                continue
            tree1.append(queue[0].val)
            node=queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append("Null")
            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append("Null")
                
        tree2=[]
        queue.append(q)
        while len(queue)>0:
            if queue[0] is "Null":
                tree2.append(None)
                queue.pop(0)
                continue
            tree2.append(queue[0].val)
            node=queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            else:
                queue.append("Null")
            if node.right is not None:
                queue.append(node.right)
            else:
                queue.append("Null")
                
        for i in range(len(tree1)):
            if tree1[i]!=tree2[i]:
                return False
        else:
                return True
