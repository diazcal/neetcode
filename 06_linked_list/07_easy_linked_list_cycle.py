"""
https://leetcode.com/problems/linked-list-cycle/
Check leetcode for the full explanation with pictures



Given head, the head of a linked list, determine if the linked list has a cycle in it

There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer
is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation:    There is a cycle in the linked list,
                where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation:    There is a cycle in the linked list,
                where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation:    There is no cycle in the linked list.
 
Constraints:
The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

# This is a O(n) time algo


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_head(list_of_values):
    first_val = list_of_values.pop(0)
    head = Node(first_val)
    current_node = head
    for n in list_of_values:
        new_node = Node(n)
        if n == 2:
            to_link_later = new_node
        current_node.next = new_node
        current_node = current_node.next
    current_node.next = to_link_later
    return head


class Solution:
    def has_cycle(self, head: Node) -> bool:
        value_set = set()
        current_node = head
        while current_node:
            if current_node.value in value_set:
                return True
            value_set.add(current_node.value)
            current_node = current_node.next
        return False


nodes = [3, 2, 0, -4]
triky_node = Node(69)
triky_node.next = triky_node
linked_nodes = create_head(nodes)
solution = Solution()
print(solution.has_cycle(linked_nodes))


# Mi respuesta a la followup question: si tuvieramos una tail podríamos comprobar si
# el tail.next es None o no, entonces lo solucionamos en O(1)


class NeetSolution:
    def has_cycle(sef, head: Node) -> bool:
        """
        En la primera solucion de Neet mete el propio nodo porque podría haber
        valores duplicados y así nos aseguramos. Pero es un hashset como el mio :-)

        Ahora bien, la solución que implementa es con el algoritmo:
        Floyd's Turtle and Hare, con el puntero lento y el puntero rapido.

        De esta manera no hace falta un hashset y podemos resolver con O(1) de
        space memory (así si no tiene tail lo podemos resolver igual de rapido)
        """

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


solution = NeetSolution()
print(solution.has_cycle(linked_nodes))
