# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode]) -> [bool, int]: # depth 계산
            if not root: # empty tree
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and # left, right의 balanced 여부
                        abs(left[1] - right[1]) <= 1) # left, right depth 비교

            return [balanced, 1 + max(left[1], right[1])] # balanced 여부, depth

        return dfs(root)[0]
