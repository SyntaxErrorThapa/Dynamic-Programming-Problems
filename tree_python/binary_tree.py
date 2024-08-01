class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.value, end=' ')
            self.in_order(root.right)

    def pre_order(self, root):
        if root:
            print(root.value, end=' ')
            self.pre_order(root.left)
            self.pre_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.value, end=' ')

    def print_in_order(self):
        print("In-order traversal:")
        self.in_order(self.root)
        print()

    def print_pre_order(self):
        print("Pre-order traversal:")
        self.pre_order(self.root)
        print()

    def print_post_order(self):
        print("Post-order traversal:")
        self.post_order(self.root)
        print()

# Example usage:
tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

tree.print_in_order()    # Output: 20 30 40 50 60 70 80
tree.print_pre_order()   # Output: 50 30 20 40 70 60 80
tree.print_post_order()  # Output: 20 40 30 60 80 70 50
