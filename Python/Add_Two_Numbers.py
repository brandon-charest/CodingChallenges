""" 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in
reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    l3 = ListNode(0)
    dummy = l3
    carry = 0
    while l1 or l2:
        total = carry

        if l1:
            total += l1.val
        if l2:
            total += l2.val

        dummy.next = ListNode(total % 10)
        carry = total // 10
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        dummy = dummy.next

    if carry > 0:
        dummy.next = ListNode(carry)
    return l3.next


x = ListNode(2)
x.next = ListNode(4)
x.next.next = ListNode(3)

y = ListNode(5)
y.next = ListNode(6)
y.next.next = ListNode(4)

result = add_two_numbers(x, y)

