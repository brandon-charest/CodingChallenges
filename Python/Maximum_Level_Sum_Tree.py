""" 1161. Maximum Level Sum of a Binary Tree
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 
Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
"""
from Coding.Binary_Tree import Tree
from collections import deque

nodes = [1,7,0,7,-8]
tree = Tree()
tree.add(nodes)


def max_level_sum(root: Tree) -> int:
    max_sum, cur_level, max_level = -float('inf'), 0, 0
    q = deque()
    q.append(root)
    while q:
        cur_level += 1
        cur_sum = 0
        for _ in range(len(q)):
            node = q.popleft()
            cur_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if max_sum < cur_sum:
            max_sum, max_level = cur_sum, cur_level
    return max_level


print(max_level_sum(tree.root()))
