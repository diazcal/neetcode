"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list,
reverse the list, and return the reversed list.
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    """
    For this given example we need only the append method to build the single list.
    """

    def __init__(self, nodes=None):
        self.head = None
        self._length = 0
        if nodes is not None:
            node = ListNode(nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = ListNode(element)
                node = node.next
                self._increase_len_by_one()

    def _increase_len_by_one(self):
        self._length += 1

    def _decrease_len_by_one(self):
        self._length -= 1

    def __len__(self):
        return self._length

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        # RealPyhon (without making use of __iter__())
        # node = self.head
        # nodes = []
        # while node is not None:
        #     nodes.append(str(node.value))
        #     node = node.next
        # nodes.append("None")
        # return " -> ".join(nodes)

        # Mix of RealPython and mine (making use of __iter__())
        list_of_nodes = []
        for node in self:
            list_of_nodes.append(str(node.value))
        return " -> ".join(list_of_nodes)

    def prepend(self, value: int):
        # RealPython & ZeroToMastery
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
        self._increase_len_by_one()

    def append(self, value: int):
        # ZeroToMastery ---> with tail
        # O(1)
        new_node = ListNode(value)
        self.tail.next = new_node
        self.tail = new_node
        self._length += 1

        # # RealPython ---> without tail and traversing the whole list
        # # O(n)
        # if self.head is None:
        #     self.head = node
        #     return
        # for current_node in self:
        #     # This is the traverse part. We do nothing until we reach the end
        #     pass
        # current_node.next = node


class Solution:
    def reverse_list(self, linked_list: SingleLinkedList):
        prev, current = None, linked_list.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        linked_list.head = prev


single_linked_list = SingleLinkedList([99, 8, 22])
single_linked_list.prepend(1)
single_linked_list.prepend(2)
single_linked_list.prepend(3)
single_linked_list.prepend(4)
single_linked_list.prepend(5)

print(single_linked_list)
solution = Solution()
solution.reverse_list(single_linked_list)
print(single_linked_list)