class _Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList:
    def __init__(self, head=None):
        self._head = head
        self._size = 0

    def add_node(self, data):
        new_node = _Node(data, self._head)
        self._head = new_node
        self._size += 1
        return True

    def print(self):
        current = self._head
        while current:
            print(current.data, "->", end=' ')
            current = current.get_next()
        print()

    def is_empty(self):
        return self._head is None

    def get_head_node(self):
        return self._head

    def get_node_value(self,node: _Node) -> int:
        return node.data
