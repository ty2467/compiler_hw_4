class Node:
    def __init__(self, node_type, children=None, value=None):
        self.node_type = node_type  # e.g., 'Assign', 'Call'
        self.children = children if children else []  # List of child nodes
        self.value = value  # Optional value, like a constant or variable name

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value}, children={self.children})"



# x = 2 + 3        # This can be folded to x = 5
# y = x * 4        # Uses the folded constant for x
# z = y - 10       # Uses the folded constant for y

module_node1 = Node("Module", children=[
    # Line 1: x = 2 + 3
    Node("Assign", value="=", children=[
        Node("Name", value="x"),           # LHS
        Node("BinOp", value="+", children=[
            Node("Constant", value=2),     # Operand: 2
            Node("Constant", value=3)      # Operand: 3
        ])
    ]),
    # Line 2: y = x * 4
    Node("Assign", value="=", children=[
        Node("Name", value="y"),           # LHS
        Node("BinOp", value="*", children=[
            Node("Name", value="x"),       # Operand: x
            Node("Constant", value=4)      # Operand: 4
        ])
    ]),
    # Line 3: z = y - 10
    Node("Assign", value="=", children=[
        Node("Name", value="z"),           # LHS
        Node("BinOp", value="-", children=[
            Node("Name", value="y"),       # Operand: y
            Node("Constant", value=10)     # Operand: 10
        ])
    ])
])


# x = 5          # Constant assignment
# y = x + 3      # Can propagate x as 5, making y = 5 + 3
# z = y * 2      # Can propagate y as 8, making z = 8 * 2

module_node2 = Node("Module", children=[
    # Line 1: x = 5
    Node("Assign", value="=", children=[
        Node("Name", value="x"),           # LHS
        Node("Constant", value=5)          # RHS
    ]),
    # Line 2: y = x + 3
    Node("Assign", value="=", children=[
        Node("Name", value="y"),           # LHS
        Node("BinOp", value="+", children=[
            Node("Name", value="x"),       # Operand: x
            Node("Constant", value=3)      # Operand: 3
        ])
    ]),
    # Line 3: z = y * 2
    Node("Assign", value="=", children=[
        Node("Name", value="z"),           # LHS
        Node("BinOp", value="*", children=[
            Node("Name", value="y"),       # Operand: y
            Node("Constant", value=2)      # Operand: 2
        ])
    ])
])

a = 5 + 3          # Simple addition
b = a * 2          # Multiplication can be reduced to b = a + a
c = b * 2          # Another multiplication reducible to c = b + b

module_node3 = Node("Module", children=[
    # Line 1: a = 5 + 3
    Node("Assign", value="=", children=[
        Node("Name", value="a"),           # LHS
        Node("BinOp", value="+", children=[
            Node("Constant", value=5),     # Operand: 5
            Node("Constant", value=3)      # Operand: 3
        ])
    ]),
    # Line 2: b = a * 2
    Node("Assign", value="=", children=[
        Node("Name", value="b"),           # LHS
        Node("BinOp", value="*", children=[
            Node("Name", value="a"),       # Operand: a
            Node("Constant", value=2)      # Operand: 2
        ])
    ]),
    # Line 3: c = b * 2
    Node("Assign", value="=", children=[
        Node("Name", value="c"),           # LHS
        Node("BinOp", value="*", children=[
            Node("Name", value="b"),       # Operand: b
            Node("Constant", value=2)      # Operand: 2
        ])
    ])
])


# a = 10          # Original value assignment
# b = a           # Copy of a
# c = b + 5       # Can propagate b as a, making c = a + 5

module_node4 = Node("Module", children=[
    # Line 1: a = 10
    Node("Assign", value="=", children=[
        Node("Name", value="a"),           # LHS
        Node("Constant", value=10)         # RHS
    ]),
    # Line 2: b = a
    Node("Assign", value="=", children=[
        Node("Name", value="b"),           # LHS
        Node("Name", value="a")            # RHS
    ]),
    # Line 3: c = b + 5
    Node("Assign", value="=", children=[
        Node("Name", value="c"),           # LHS
        Node("BinOp", value="+", children=[
            Node("Name", value="b"),       # Operand: b
            Node("Constant", value=5)      # Operand: 5
        ])
    ])
])
