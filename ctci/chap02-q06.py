from simple_linked_list import LinkedList


def is_palindrome(lst: LinkedList) -> bool:
    # Input size parameter : n ≝ len(lst)
    # Time complexity : linear
    stack = list(lst)
    for value in lst:
        # we never enter the loop if lst is empty
        if not stack.pop() == value:
            return False
    return True


if __name__ == "__main__":
    for values in [[], [1], [1, 2, 3], [1, 2, 4, 2, 1], [1, 1, 1]]:
        lst = LinkedList(values)
        res = is_palindrome(lst)
        print(f"{list(lst)} is{'' if res else ' not'} a palindrome")
