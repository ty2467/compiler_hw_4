#AST-Flatten generates more pseudo assembly. this is for mips
import node_class_4


#trouble: have to
tiles_hash = {
    "+":
        {"pattern": "BinaryOp", "instruction": "add {dest}, {src1}, {src2}", "cost": 1},
    "*":
        {"pattern": "BinaryOp", "instruction": "mul {dest}, {src1}, {src2}", "cost": 1}, #the uniformity of cost may not be right. idk
        #but i read you need cost for maximal munch.
    "=":
        {"pattern": "Assign", "instruction": "sw {computed_temp}, {variable_address}", "cost": 3},
    "-":
        {"pattern": "BinaryOp", "instruction": "sub {dest}, {src1}, {src2}", "cost": 1},
    "/":
        {"pattern": "BinaryOp", "instruction": "div {dest}, {src1}, {src2}", "cost": 1}
    }

# temp_count = 0
instructions = []
available_temporary_registers = ["$t9", "$t8", "$t7", "$t6", "$t5", "$t4", "$t3", "$t2", "$t1"] #we have to work with real registers, not imaginary registers anymore.
busy_temporary_registers = []


def traverse(node):

    global instructions
    global available_temporary_registers
    global busy_temporary_registers


    if not node.children: # return the instruction if you are the leaf

        register_in_use1 = available_temporary_registers.pop()#for the value
        busy_temporary_registers.append(register_in_use1)
        register_in_use2 = available_temporary_registers.pop()#for the return value of memory


        # instruction =  f"li temp{temp_count}, {node.value}"
        #system call for memory
        memory_instructions = [f"lw {register_in_use1} {node.value} ", "li $v0, 9", "li $a0, 4", "syscall", f"move {register_in_use2}, $v0",  f"sw {register_in_use1} {register_in_use2}"] #request one word
        available_temporary_registers.append(busy_temporary_registers.pop())
        busy_temporary_registers.append(register_in_use2)


        for ins in memory_instructions:
            instructions.append(ins)

        '''
            Later after register allocation, when I see the variables mapped to their registers, 
            I will do this 
        '''
        return register_in_use2


    else:
        child_computation_results = []
        for child in node.children:
            child_computation_results.append( traverse(child) )

        # print(node.node_type, node.value)
        if node.value in tiles_hash:

            instruction_template = tiles_hash[node.value]["instruction"]
            instruction = ""
            result_register = available_temporary_registers.pop()
            busy_temporary_registers.append(result_register)

            if tiles_hash[node.value]["pattern"]  == "BinaryOp": #same for all four, left div right, left minus right.
                instruction = instruction_template.format(dest = f"{result_register}", src1 = child_computation_results[0], src2 = child_computation_results[1])
            elif tiles_hash[node.value]["pattern"] == "Assign":
                instruction = instruction_template.format(computed_temp = child_computation_results[1], variable_address = child_computation_results[0])

            instructions.append(instruction)


            return result_register

        #without else statement, only one = assignment max is computed. multiline is not handled.
        #else


import optimize
def main():
    global instructions
    # global temp_count
    j = 0
    for a in node_class_4.module_nodes:
        j += 1
        # temp_count = 0
        instructions = []

        '''
            Optimize, new code for integrating with hw4, ln96~101.
        '''
        print(f"log: pre optimized tree: {a} \n\n")

        optimize.constant_table = {}
        optimize.copy_table = {}

        optimize.optimize_traverse(a, optimize.constant_folding)
        optimize.optimize_traverse(a, optimize.callback_constant_propagation)
        optimize.optimize_traverse(a, optimize.callback_strength_reduction)
        optimize.optimize_traverse(a, optimize.callback_copy_propagation)
        print(f"log: optimized tree: {a} \n\n")

        final_register = traverse(a)

        num_registers = len(busy_temporary_registers)
        for i in range(num_registers):
            available_temporary_registers.append(busy_temporary_registers.pop()) #clean up registers
        print(instructions)


        with open(f"assembly_module_{j}.asm", "w") as file: #
            file.seek(0)
            for instruction in instructions:
                file.write(instruction + "\n")


if __name__ == "__main__":
    main()





