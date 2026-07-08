from CH09L04_node import Node


class LinkedList:
    def add_to_tail(self, node: Node) -> None:
        if self.head is None:
            self.head = node 
            return 

        last = self.head
        for n in self:
            last = n

        last.next = node

    # don't touch below this line

    def __init__(self) -> None:
        self.head: Node | None = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

