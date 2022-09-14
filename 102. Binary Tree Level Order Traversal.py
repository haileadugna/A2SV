# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            arr = []
            for i in range(n):
                node = q.popleft()
                if node:
                    arr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if arr:
                ans.append(arr)
        return ans