# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return 
        queue=[]
        result=[]
        queue.append(root)
        while len(queue)>0:
            size=len(queue)
            level=[]
            while size>0:
                node=queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                size-=1
            result.append(level)
        return result[::-1]
        
