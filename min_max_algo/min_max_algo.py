class Tree:
    def __init__(self, children):
        self.children = children

    # This is like Java's toString() for human-readable output
    def __str__(self):
        return self._print_tree(0)

    # This is more like an official or unambiguous representation of the object
    def __repr__(self):
        return f"Tree({self.children})"

    # Helper method to print tree with indentation
    def _print_tree(self, level):
        result = "  " * level + "Tree\n"
        for child in self.children:
            result += child._print_tree(level + 1)
        return result

class Terminal(Tree):
    def __init__(self, value):
        super().__init__([])  # Terminal node has no children
        self.value = value  # Sets the value for the terminal node

    # Like Java's toString() to return a user-friendly value
    def __str__(self):
        return f"Terminal({self.value})"

    # More detailed, unambiguous representation
    def __repr__(self):
        return f"Terminal({self.value})"

    def _print_tree(self, level):
        return "  " * level + f"Terminal({self.value})\n"
        
    def minmax(self, tree, maximising_player):
        
        # Check if the tree is instance of the terminal or terminal node 
        if isinstance(tree, Terminal):
            return tree.value
        
        if maximising_player:
            max_ = float("-inf")
            for subtree in tree.children:
                max_ = max(self.minmax(subtree, not maximising_player), max_)
            return max_
        
        else:
            min_ = float("+inf")
            for subtree in tree.children:
                min_ = min(self.minmax(subtree, not maximising_player), min_)
            return min_

    def alpha_beta_pruning(self, tree, maximizing, alpha=float("-inf"), beta=float("+inf")):
        print(tree.__str__)
        # Base case 
        if isinstance(tree, Terminal):
            return tree.value
        
        if maximizing:
            max_ = float("-inf")
            for subtree in tree.children:
                max_ = max(self.alpha_beta_pruning(subtree, not maximizing, alpha, beta), max_)
                alpha = max(alpha, max_)
                if alpha >= beta:
                    break
            return max_
        else:
            min_ = float("inf")
            for subtree in tree.children:
                min_ = min(self.alpha_beta_pruning(subtree, not maximizing, alpha, beta), min_)
                beta = min(min_, beta)
                if alpha >= beta:
                    break
            return min_
            
tree = Tree([
    Tree([
        Tree([
            Terminal(3),
            Terminal(4),
        ]),
        Tree([
            Terminal(8),
            Tree([
                Terminal(-2),
                Terminal(10),
            ]),
            Terminal(5),
        ])
    ]),
    Terminal(7),
])

terminal = Terminal(None)

result = terminal.alpha_beta_pruning(tree, True)
print(result)

            
    