class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self, values: list = None):
        self.head = None
        self._len = 0
        if values:
            for value in values:
                new_node = Node(value)
                if not self.head:
                    self.head = new_node
                    self.tail = self.head
                    self._increase_len()
                    continue
                self.tail.next = new_node
                self.tail = new_node
                self._increase_len()
            return
        self.tail = self.head
        
    def _increase_len(self):
        self._len += 1

    def _decrease_len(self):
        self._len -= 1

    def __len__(self):
        return self._len

    def _traverse(self, index):
        current_node = self.head
        if len(self) <= index:
            raise Exception("Too long man")
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    def __repr__(self):
        list_of_nodes = []
        for node in self:
            list_of_nodes.append(str(node.value))
        return " -> ".join(list_of_nodes)

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self._increase_len()

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = self.head
            return
        self.tail.next = new_node
        self.tail = new_node
        self._increase_len()

    def insert_before(self, value, index):
        if index == 0:
            self.prepend(value)
            return
        elif index == len(self):
            self.append(value)
            return
        elif index > len(self):
            raise IndexError
        new_node = Node(value)
        prev_node = self.head
        for index_node, node in enumerate(self):
            if index_node == index:
                new_node.next = node
                prev_node.next = new_node
                self._increase_len()
                return
            prev_node = node

    def insert_after(self, value, index):
        new_node = Node(value)
        if index >= len(self):
            raise IndexError
        for index_node, node in enumerate(self):
            if index_node == index:
                new_node.next = node.next
                node.next = new_node
                self._increase_len()
                return

    def reverse(self):
        previous_p, current_p = None, self.head
        while current_p:
            next_p = current_p.next
            current_p.next = previous_p
            previous_p = current_p
            current_p = next_p
        self.head = previous_p
        

if __name__ == "__main__":
    single_linked_list = SingleLinkedList()
    single_linked_list = SingleLinkedList([2, 3, 9])
    print(single_linked_list, f"size: {len(single_linked_list)}")
    single_linked_list.prepend(19)
    print(single_linked_list, f"size: {len(single_linked_list)}")
    single_linked_list.append(123)
    print(single_linked_list, f"size: {len(single_linked_list)}")
    single_linked_list.insert_before(6969, 5)
    print(single_linked_list, f"size: {len(single_linked_list)}")
    single_linked_list.insert_after(123456, 5)
    print(single_linked_list, f"size: {len(single_linked_list)}")
    single_linked_list.reverse()
    print(single_linked_list)