class Tree:
    def __init__(self, children):
        self.children = children
        
class Terminal(Tree):
    def __init__(self, value):
        super().__init__([]) # Meaning that terminal node has no children 
        self.value = value # Sets the value for the terminal node 
        
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

result = terminal.minmax(tree, True)
print(result)

            
    