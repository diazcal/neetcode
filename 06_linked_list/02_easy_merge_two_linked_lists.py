from linked_list_from_scratch import SingleLinkedList as SList
from linked_list_from_scratch import Node

list_a = SList([1, 2, 4])
list_b = SList([1, 3, 4, 5])

print(list_a)
print(list_b)


class Solution:
    """
    Mi solucion implementa mi propio LinkedList.
    En mi LinledList el append es de O(1), así que en el merge al tener un for
    con doble puntero, me sale que la operación es:
        - Time:     O(n)
        - Space:    O(1) con una SingleLinkedList en memoria que devuelvo luego

    Una optimización quizás podría ser meter una de las dos en la otra a la vez que
    las recorro y así me ahorro tener en memoria otra linkedlist, y para eso necesito
    implementar algún tipo de "insert()" en el indice en el que me encuentro
    al mismo tiempo que loopeo las dos listas.
    """

    def merge_two_lists(self, list1: SList, list2: SList) -> SList:
        combined_list = SList()
        max_range = max(len(list1), len(list2))
        head1 = list1.head
        head2 = list2.head
        for _ in range(max_range):
            if head1 and head2:
                if head1.value < head2.value:
                    combined_list.append(head1.value)
                    combined_list.append(head2.value)
                else:
                    combined_list.append(head2.value)
                    combined_list.append(head1.value)
                head1 = head1.next
                head2 = head2.next
                continue
            elif head1 and not head2:
                combined_list.append(head1.value)
                head1 = head1.next
                continue
            elif not head1 and head2:
                combined_list.append(head2.value)
                head2 = head2.next
                continue
        return combined_list


sol = Solution()
merged_list = sol.merge_two_lists(list_a, list_b)
print(merged_list)


class NeetSolution:
    """
    His solution uses only the "head" of a single linked list and does not create a
    class for it, it just has the head an the tail over there and builds the list
    at the time it iterates the values.

    As he initializes dummy head with 0 to avoid any edge scenario,
    he returns dummy_head at the end of the function because the first node is
    dummy.
    """

    def merge_two_lists(self, list1: SList, list2: SList) -> Node:
        dummy_head = Node(0)
        tail = dummy_head
        l1_node = list1.head
        l2_node = list2.head

        while l1_node and l2_node:
            if l1_node.value < l2_node.value:
                tail.next = l1_node
                l1_node = l1_node.next
            else:
                tail.next = l2_node
                l2_node = l2_node.next
            tail = tail.next

        if l1_node:
            tail.next = l1_node
        elif l2_node:
            tail.next = l2_node
        return dummy_head.next


sol = NeetSolution()
merged_list = sol.merge_two_lists(list_a, list_b)
print(merged_list)
