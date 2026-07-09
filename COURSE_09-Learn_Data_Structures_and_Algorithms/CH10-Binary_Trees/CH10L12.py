from typing import Any

"""
Complete the height method. It returns the height of the tree rooted at the current node
If the nodes value is None, return 0.
Recursively calculate the height of the left subtree.
Recursively calculate the height of the right subtree.
Use the max() function to return the maximum of the left and right subtree heights plus 1.
"""

class BSTNode:
    def height(self) -> int:
        if self.val is None:
            return 0

        left_height = self.left.height() if self.left is not None else 0
        right_height = self.right.height() if self.right is not None else 0
        
        return max(left_height, right_height) + 1

    # don't touch below this line

    def __init__(self, val: Any = None) -> None:
        self.left: "BSTNode | None" = None
        self.right: "BSTNode | None" = None
        self.val = val

    def insert(self, val: Any) -> None:
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

