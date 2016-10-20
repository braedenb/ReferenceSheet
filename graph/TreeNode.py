class Node:
    def __init__(self, value):
        # initially, this node has no parent, nor any children
        self.value = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        # to add a child, add the passed node to the list of children,
        # but also link it back to "self", which is the parent
        child.parent = self
        self.children.append(child)

def traverse(root, do_something):
    # This is the list of nodes we have yet to visit. We start with just
    # the root
    to_visit = [root]

    # while there are more nodes to visit
    while len(to_visit) is not 0:
        # get the next node to visit.
        # Note: to_visit.pop() gives a Depth-First-Search
        # to_visit.pop(0) gives a Breadth-First-Search
        # check out https://en.wikipedia.org/wiki/Tree_traversal
        #next_node = to_visit.pop()
        next_node = to_visit.pop(0)

        # Add all of the children of this node as nodes to visit
        to_visit.extend(next_node.children)

        # do something with the node (we passed the "action" as a parameter)
        do_something(next_node)

# Building a tree here
A = Node('A')

# First level
B = Node('B')
A.add_child(B)
C = Node('C')
A.add_child(C)

# Second level
D = Node('D')
B.add_child(D)
E = Node('E')
B.add_child(E)

F = Node('F')
C.add_child(F)

# Call the traverse function with a starting node, and a function to
# perform at each node
traverse(A, lambda node : print(node.value))
