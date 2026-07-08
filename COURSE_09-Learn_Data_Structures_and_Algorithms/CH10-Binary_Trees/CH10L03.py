from typing import Any


class BSTNode:
    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if self.val is None:
            self.val = val
            return 

        if self.val == val:
            return
        
        if val < self.val:
            if self.left is None:
                self.left = BSTNode(val)
                return
            else:
                self.left.insert(val)
                return
        # val > self.val
        if self.right is None:
            self.right = BSTNode(val)
        else:
            self.right.insert(val)


