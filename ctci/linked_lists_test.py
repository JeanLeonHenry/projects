import unittest

from linked_lists import ListNode, LinkedList


class TestNode(unittest.TestCase):
    def test_print_single_node(self):
        node = ListNode(3)
        self.assertEqual(str(node), "3 -> None")

    def test_print_two_nodes(self):
        head = ListNode(3, ListNode(4))
        self.assertEqual(str(head), "3 -> 4 -> None")


class TestList(unittest.TestCase):

    def test_build_list(self):
        head = LinkedList(ListNode(3, ListNode(4)))
        self.assertEqual(str(head), "[3, 4]")

    def test_build_list_from_values(self):
        values = list(range(3))
        head = LinkedList.from_list(values)
        self.assertEqual(str(head), str(values))

    def test_build_from_no_values(self):
        head = LinkedList.from_list([])
        self.assertIsNone(head.head)

    def test_append_list(self):
        head = LinkedList(ListNode(3))
        head.append(ListNode(4))
        self.assertEqual(str(head), "[3, 4]")

    def test_append_to_empty_list(self):
        head = LinkedList(None)
        head.append(ListNode(4))
        self.assertEqual(str(head), "[4]")

    def test_add_lists(self):
        list1 = LinkedList.from_list(list(range(3)))
        list2 = LinkedList.from_list(list(range(3, 6)))
        result = LinkedList.from_list(list(range(6)))
        self.assertEqual(str(list1+list2), str(result))

    def test_pop(self):
        values = [0, 1, 2]
        linked_list = LinkedList.from_list(values)
        values.pop(0)
        linked_list.pop()
        self.assertEqual(str(linked_list), str(LinkedList.from_list(values)))

    def test_pop_one_element(self):
        linked = LinkedList(ListNode())
        linked.pop()
        self.assertIsNone(linked.head)

    def test_length(self):
        for values in [[], [1, 2]]:
            with self.subTest(values=values):
                self.assertEqual(
                    len(LinkedList.from_list(values)), len(values))

    def test_iterating(self):
        for values in [[], [1, 2]]:
            with self.subTest(values=values):
                linked = LinkedList.from_list(values)
                self.assertEqual([el for el in linked], values)
