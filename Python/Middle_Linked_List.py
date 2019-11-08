from Structure.Linked_List import SinglyLinkedList


def middle_linked_list(link_list: SinglyLinkedList):
    slow = fast = link_list.get_head_node()

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
