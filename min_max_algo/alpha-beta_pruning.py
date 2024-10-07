class Tree:
    def __init__(self, children):
        self.children = children

    def is_terminal(self):
        return len(self.children) == 0

    def __str__(self):
        return self._print_tree(0)

    def _print_tree(self, level):
        result = "  " * level + "Tree\n"
        for child in self.children:
            result += child._print_tree(level + 1)
        return result

class Terminal(Tree):
    def __init__(self, value):
        super().__init__([])
        self.value = value

    def is_terminal(self):
        return True

    def utility(self):
        return self.value

    def _print_tree(self, level):
        return "  " * level + f"Terminal({self.value})\n"

# Alpha-Beta Pruning functions
def alpha_beta_search(tree):
    value, move = max_value(tree, float('-inf'), float('inf'))
    return value, move

def max_value(tree, alpha, beta):
    if tree.is_terminal():
        return tree.utility(), None

    v = float('-inf')
    best_move = None
    for i, child in enumerate(tree.children):
        v2, _ = min_value(child, alpha, beta)
        if v2 > v:
            v = v2
            best_move = i  # Track the index of the best move
        alpha = max(alpha, v)
        if v >= beta:
            break  # Beta cut-off
    return v, best_move

def min_value(tree, alpha, beta):
    if tree.is_terminal():
        return tree.utility(), None

    v = float('inf')
    best_move = None
    for i, child in enumerate(tree.children):
        v2, _ = max_value(child, alpha, beta)
        if v2 < v:
            v = v2
            best_move = i  # Track the index of the best move
        beta = min(beta, v)
        if v <= alpha:
            break  # Alpha cut-off
    return v, best_move

# Define the tree based on your previous example
tree = Tree([
    Tree([
        Tree([
            Terminal(8),
            Terminal(23),
            Terminal(-47),
            Terminal(28)
        ]),
        Tree([
            Terminal(-30),
            Terminal(-37),
            Terminal(3),
            Terminal(-41)
        ])
    ]),
    Tree([
        Tree([
            Terminal(-19),
            Terminal(4),
            Terminal(-49),
            Terminal(4)
        ]),
        Tree([
            Terminal(43),
            Terminal(45),
            Terminal(-26),
            Terminal(-14)
        ])
    ])
])

# Run alpha-beta search
value, best_move = alpha_beta_search(tree)
print(f"Best move index: {best_move}, value is {value}")
