from typing import List


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Tree:
    def __init__(self):
        self._root = None

    def root(self):
        return self._root

    def add(self, val):
        if type(val) is list:
            self._add_multiple(val)
        elif type(val) is int:
            self._add(val, self._root)
        else:
            print(f'Invalid type added [{type(val)} ], only accepts int or List[int]')

    def _add_multiple(self, val_list: List[int]):
        for v in val_list:
            self._add(v, self._root)

    def _add(self, val, node):
        if self._root is None:
            self._root = Node(val)
            return
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self._root is None:
            return None
        else:
            return self._find(val, self._root)

    def _find(self, val, node) -> int:
        if val is node.val:
            return node
        elif val < node.val and node.left is not None:
            return self._find(val, node.left)
        elif val > node.val and node.right is not None:
            return self._find(val, node.right)

    def print_tree(self, traversal='in'):
        if self._root is not None:
            self._print(self._root,traversal.lower())

    def _print(self, root,traversal):
        if traversal == 'in':
            self._inorder(root)
        elif traversal == 'pre':
            self._preorder(root)
        elif traversal == 'post':
            self._postorder(root)
        else:
            self._inorder(root)

    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(node.val)
            self._inorder(node.right)

    def _preorder(self, node):
        if node is not None:
            print(node.val)
            self._preorder(node.left)
            self._preorder(node.right)

    def _postorder(self, node):
        if node is not None:
            self._postorder(node.left)
            self._postorder(node.right)
            print(node.val)
