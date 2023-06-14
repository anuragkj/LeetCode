# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev = None
        diff = float("inf")

        
        def DFS(node):
            nonlocal prev, diff
            if node == None:
                return
            DFS(node.left)
            if prev:
                diff = min(diff, node.val - prev.val)
            prev = node
            DFS(node.right)

        DFS(root)
        return diff


#####Practicing BST
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None

# class BST:
#     def __init__(self, val = 0):
#         self.root = TreeNode(val)

#     def insert(self, val):
#         cur_root = self.root
#         while(cur_root):
#             print(cur_root.val)
#             if val>= cur_root.val:
#                 cur_root = cur_root.right
#             else:
#                 cur_root = cur_root.left
            
#         cur_root = TreeNode(val)

#     def DFS(self, node):
#         if not node:
#             return
        
#         self.DFS(node.left)
#         print(node.val)
#         self.DFS(node.right)

# lst = [4,2,6,1,3]
# obj = BST(4)
# for i in lst[1:]:
#     obj.insert(i)
# # print(obj.root.val)
# # print(obj.root.right.val)
# obj.DFS(obj.root)




