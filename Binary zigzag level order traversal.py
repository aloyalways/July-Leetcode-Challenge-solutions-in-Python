# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return root
        queue=[]
        result=[]
        queue.append(root)
        zigzag=False
        while len(queue)>0:
            size=len(queue)
            level=[]
            while size>0:
                node=queue[0]
                level.append(node.val)
                queue.pop(0)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                size-=1
            if zigzag:
                result.append(level[::-1])
                zigzag=False
            else:
                result.append(level)
                zigzag=True
        return result
