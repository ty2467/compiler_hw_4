import node_class_4

constant_table = {}
copy_table = {}
def traverse(node, callback):
    if not node.children:
        return node
    else:
        for child in node.children:
            for child in node.children:
                traverse(child)
            traverse(child, callback)
            maybe_cleaned_node = callback(node) #make sure the
            return maybe_cleaned_node

def _callback_constant_folding(node):
    if node.node_type == "BinOp":
        values = []
        if node.children[0].node_type == "Constant":
            values.append(node.children[0].value)
        else:
            return node
        if node.children[1].node_type == "Constant":
            values.append(node.children[1].value)
        else:
            return node

        folded_constant = None
        if node.value == "+":
            folded_constant = values[0] + values[1]
        elif node.value == "-":
            folded_constant = values[0] - values[1]
        elif node.value == "*":
            folded_constant = values[0] * values[1]
        elif node.value == "/":
            folded_constant = values[0] / values[1]

        new_node = node_class_4.module_node("Constant", None, value = folded_constant)

        return new_node
    else:
        return node


def _callback_constant_propagation(node):
    global constant_table
    if node.node_type == "Assign":
        if node.children[1].node_type == "Constant":
            constant_table[node.children[0].value] = node.children[1].value
        elif node.children[1].node_type == "Name" and node.children[1].value in constant_table:
            node.children[1].node.value = constant_table[node.children[1].value]
            node.children[1].node_type = "Constant"
        elif node.children[0].node_type == "Name" and node.children[0].value in constant_table:
            node.children[0].node.value = constant_table[node.children[0].value]
            node.children[0].node_type = "Constant"
        else:
            return node
        return node
    else:
        return node


def _callback_strength_reduction(node):
    if node.node_type == "BinOp":
        if node.value == "*":
            if node.children[1].node_value == 2:
                node.children[1].node_type = node.children[0].node_type
                node.children[1].node_value = node.children[1].value
                node.value = "+"
                return node
    else:
        return node


def _callback_copy_propagation(node):
    global copy_table
    if node.node_type == "Constant":
        return node
    else:
        if node.node_type == "BinOp":
            if node.children[0].node_type == "Name" and node.children[0].value in copy_table:
                node.children[0].node.value = copy_table[node.children[0].value]
            if node.children[1].node_type == "Name" and node.children[1].value in copy_table:
                node.children[1].node.value = copy_table[node.children[1].value]
        elif node.node_type == "Assign":
            if node.children[1].node_type == "Name" and node.children[1].value not in copy_table:
                if node.children[0].node_type == "Name":
                    copy_table[node.children[0].node.value] = node.children[1].node.value
            elif node.children[1].node_type == "Name" and node.children[1].value in copy_table:
                node.children[1].node.value = copy_table[node.children[1].value] #you propagate and get the original variable

