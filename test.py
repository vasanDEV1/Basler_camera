class Node:
    def __init__(self, value, data):
        self.value = value
        self.data = data
        self.next = None
        self.previous = None
        self.first_child = None
        self.parent = None

    def __repr__(self):
        return f"Node(value={self.value}, data={self.data}, next={self.next.value if self.next else None}, previous={self.previous.value if self.previous else None}, first_child={self.first_child.value if self.first_child else None}, parent={self.parent.value if self.parent else None})"

def build_tree(data):
    nodes = {}

    # Create all nodes
    for i, (next_node, previous, first_child, parent) in enumerate(data):
        nodes[i] = Node(i, None)

    # Link nodes
    for i, (next_node, previous, first_child, parent) in enumerate(data):
        if next_node != -1:
            nodes[i].next = nodes[next_node]
        if previous != -1:
            nodes[i].previous = nodes[previous]
        if first_child != -1:
            nodes[i].first_child = nodes[first_child]
        if parent != -1:
            nodes[i].parent = nodes[parent]

    return nodes

# Reinitialize data
data = [
    [-1, -1,  1, -1],
    [ 2, -1, -1,  0],
    [ 3,  1, -1,  0],
    [ 4,  2, -1,  0],
    [ 5,  3, -1,  0],
    [ 6,  4, -1,  0],
    [ 7,  5, -1,  0],
    [ 8,  6, -1,  0],
    [ 9,  7, -1,  0],
    [10,  8, -1,  0],
    [11,  9, -1,  0],
    [12, 10, -1,  0],
    [13, 11, -1,  0],
    [14, 12, -1,  0],
    [15, 13, -1,  0],
    [16, 14, -1,  0],
    [17, 15, -1,  0],
    [18, 16, -1,  0],
    [19, 17, -1,  0],
    [20, 18, -1,  0],
    [-1, 19, 21,  0],
    [22, -1, -1, 20],
    [23, 21, -1, 20],
    [24, 22, -1, 20],
    [25, 23, -1, 20],
    [26, 24, -1, 20],
    [27, 25, -1, 20],
    [28, 26, -1, 20],
    [29, 27, -1, 20],
    [59, 28, 30, 20],
    [31, -1, -1, 29],
    [32, 30, -1, 29],
    [33, 31, -1, 29],
    [34, 32, -1, 29],
    [35, 33, -1, 29],
    [36, 34, -1, 29],
    [37, 35, -1, 29],
    [38, 36, -1, 29],
    [39, 37, -1, 29],
    [40, 38, -1, 29],
    [41, 39, -1, 29],
    [42, 40, -1, 29],
    [43, 41, -1, 29],
    [44, 42, -1, 29],
    [45, 43, -1, 29],
    [46, 44, -1, 29],
    [47, 45, -1, 29],
    [48, 46, -1, 29],
    [49, 47, -1, 29],
    [50, 48, -1, 29],
    [51, 49, -1, 29],
    [52, 50, -1, 29],
    [53, 51, -1, 29],
    [54, 52, -1, 29],
    [55, 53, -1, 29],
    [56, 54, -1, 29],
    [57, 55, -1, 29],
    [58, 56, -1, 29],
    [-1, 57, -1, 29],
    [-1, 29, -1, 20]
]

# Rebuild the tree and draw
nodes = build_tree(data)
draw_tree(nodes)