from simple_linked_list import Node, LinkedList


def remove_inside_node(node: Node) -> None:
    if not node or not node._next:
        raise ValueError("Wrong node provided.")
    node._value = node._next._value
    node._next = node._next._next


if __name__ == "__main__":
    lst = LinkedList([5, 6, 1, 1, 2, 3, 4, 5, 5, 6, 6, 1, 5, 6, 5])
    # lst = LinkedList([5, 6, 1, 1, 2])
    n = lst._head._next._next._next
    print(f"Deleting {n._value} at pos 3 from {list(lst)}")
    remove_inside_node(n)
    print(list(lst))
