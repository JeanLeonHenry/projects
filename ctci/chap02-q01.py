from simple_linked_list import LinkedList


def remove_duplicate(lst: LinkedList) -> None:
    seen = []
    for value in lst:
        if value in seen:
            lst.delete(value)
        else:
            seen.append(value)


if __name__ == "__main__":
    lst = LinkedList([5, 6, 1, 1, 2, 3, 4, 5, 5, 6, 6, 1, 5, 6, 5])
    # lst = LinkedList([5, 6, 1, 1, 2])
    print(f"Cleaning out {list(lst)}")
    remove_duplicate(lst)
    print(list(lst))
