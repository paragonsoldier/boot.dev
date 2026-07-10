from typing import Any


class RBNode:
    def __init__(self, val: Any) -> None:
        self.red = False
        self.parent: "RBNode | None" = None
        self.val = val
        self.left: "RBNode" = self
        self.right: "RBNode" = self


class RBTree:
    def __init__(self) -> None:
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.root = self.nil

    def insert(self, val: Any) -> None:
        new_node = RBNode(val)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        
        while current is not self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val: 
                current = current.right
            else: # new_node.val == current.val
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        else:
            if new_node.val < parent.val:
                parent.left = new_node

            else:
                parent.right = new_node


