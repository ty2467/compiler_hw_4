import node_class_4



def optimize_traverse(node, callback):
    if not node.children:
        return node
    else:
        for child in node.children:
            optimize_traverse(child, callback)

        callback(node) #clean for every non child, seek to optimize




def constant_folding(node):
    if node.node_type == "BinOp":

        if node.children[0].node_type == "Constant" and node.children[1].node_type == "Constant":
            left_child_val = node.children[0].value
            right_child_val = node.children[1].value
            folded_value = None
            if node.value == "+":
                folded_value = left_child_val + right_child_val
            elif node.value == "-":
                folded_value = left_child_val - right_child_val
            elif node.value == "*":
                folded_value = left_child_val * right_child_val
            elif node.value == "/":
                folded_value = left_child_val / right_child_val

            node.value = folded_value
            node.children = []
            node.node_type = "Constant"

        else:
            return  # the return is so the traversal can keep going
    else:
        return  # you never return node, you just fix and then move on.


constant_table = {}
def callback_constant_propagation(node):
    global constant_table
    if node.node_type == "Assign":
        if node.children[1].node_type == "Constant":
            constant_table[node.children[0].value] = node.children[1].value
            return
        elif node.children[1].node_type == "Name" and node.children[1].value in constant_table: #in the constant table as a key
            node.children[1].value = constant_table[node.children[1].value]
            node.children[1].node_type = "Constant" #propagate.
            return

    elif node.node_type == "Constant":
        return
    elif node.node_type == "BinOp":
        if node.children[0].node_type == "Name" and node.children[0].value in constant_table:
            node.children[0].value = constant_table[node.children[0].value]
            node.children[0].node_type = "Constant"
        if node.children[1].node_type == "Name" and node.children[1].value in constant_table:
            node.children[1].value = constant_table[node.children[1].value]
            node.children[1].node_type = "Constant"
        return




def callback_strength_reduction(node):
    if node.node_type == "BinOp" and node.value == "*" and node.children[1].value == 2:
        left_type = node.children[0].node_type
        left_value = node.children[0].value

        node.value = "+"
        node.children[1].node_type = left_type
        node.children[1].value = left_value

        return
    else:
        return

copy_table = {}
def callback_copy_propagation(node):
    global copy_table
    if node.node_type == "Constant":
        return node

    elif node.node_type == "Assign" and node.children[0].node_type == "Name" and node.children[1].node_type == "Name":
        if node.children[1].value not in copy_table:
                copy_table[node.children[0].value] = node.children[1].value
        elif node.children[1].value in copy_table:
            node.children[1].value = copy_table[node.children[1].value] #you propagate and get the original variable

    elif node.node_type == "BinOp":
        if node.children[0].node_type == "Name" and node.children[0].value in copy_table:
            node.children[0].value = copy_table[node.children[0].value]
        if node.children[1].node_type == "Name" and node.children[1].value in copy_table:
            node.children[1].value = copy_table[node.children[1].value]

    return