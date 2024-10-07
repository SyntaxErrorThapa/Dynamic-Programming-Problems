class Tree:
    def __init__(self, children):
        self.children = children

    def __str__(self):
        return f"Tree({', '.join(str(sub) for sub in self.children)})"

class Terminal(Tree):
    def __init__(self, value):
        super().__init__([])  # Terminal node has no children
        self.value = value  # Sets the value for the terminal node

    def __str__(self):
        return f"T({self.value})"
        
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

    def pruning(self, tree, maximising_player, alpha=float("-inf"), beta=float("+inf")):
        print(str(tree))
        if isinstance(tree, Terminal):
            return tree.value

        val, func = (float("-inf"), max) if maximising_player else (float("+inf"), min)
        for subtree in tree.children:
            val = func(self.pruning(subtree, not maximising_player, alpha, beta), val)
            if maximising_player:
                alpha = max(alpha, val)
            else:
                beta = min(beta, val)
            if (maximising_player and val >= beta) or (not maximising_player and val <= alpha):
                break
        return val

    def alpha_beta_pruning(self, tree, maximizing, alpha=float("-inf"), beta=float("+inf")):
        print(tree)
        # Base case 
        if isinstance(tree, Terminal):
            return tree.value
        
        if maximizing:
            max_ = float("-inf")
            for subtree in tree.children:
                max_ = max(self.alpha_beta_pruning(subtree, False, alpha, beta), max_)
                alpha = max(alpha, max_)
                if alpha >= beta:
                    print(f"Pruning because {alpha} >= {beta}")
                    break
            return max_
        else:
            min_ = float("inf")
            for subtree in tree.children:
                min_ = min(self.alpha_beta_pruning(subtree, True, alpha, beta), min_)
                beta = min(min_, beta)
                if alpha >= beta:
                    print(f"Pruning because {alpha} >= {beta}")
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

result = terminal.alpha_beta_pruning(tree, False)
# result = terminal.pruning(tree, True)
print(result)

            
    