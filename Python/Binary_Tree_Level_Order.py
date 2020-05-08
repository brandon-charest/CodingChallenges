""" 102. Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def level_order(root):
    if not root:
        return []
    queue, res = deque([root]), []

    while queue:
        level = []
        for i in range(len(queue)):
            curr = queue.popleft()
            level.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(level)
    return res


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(level_order(tree))



