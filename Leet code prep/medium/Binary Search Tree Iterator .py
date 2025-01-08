class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._left_inorder(root)

    def _left_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._left_inorder(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0
