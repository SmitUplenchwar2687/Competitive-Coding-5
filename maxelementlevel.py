# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = []
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.helper(root, 0)
        return self.res
    def helper(self, root, depth):
        if root == None:
            return
        if len(self.res) <= depth:
            self.res.append(root.val)
        else:
            if self.res[depth] < root.val:
                self.res[depth] = root.val
        self.helper(root.left, depth+1)
        self.helper(root.right, depth+1)

        