from binary_tree import BinaryTree

def diameterOfBinaryTree(tree):
    def helper(root):
            if root is None:
                return 0
            
            result = helper(root.left) + 1
            result = helper(root.right) + 1

            return result
        
    return helper(tree.root)    

def isSameTree(p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        # Perform in order traversal
        def helper(a, b):
            if a is None and b is None:
                return True
            if a.value != b.value:
                return False
            else:
                return True
                
            left = helper(a.left, b.left)
            right = helper(a.right, b.right)

            return left and right 
        
        return helper(p, q)


def main():
    # Create an instance of BinaryTree
    tree1 = BinaryTree()
    tree2 = BinaryTree()
    # Insert elements
    tree1.insert(1)
    tree1.insert(2)
    tree1.insert(3)
    
    tree2.insert(1)
    tree2.insert(2)
    tree2.insert(3)
    # Check the diameter of the tree
    print(isSameTree(tree1.root, tree2.root))
if __name__ == "__main__":
    main()
