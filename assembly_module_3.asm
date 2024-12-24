lw $t3 a 
li $v0, 9
li $a0, 4
syscall
move $t1, $v0
sw $t3 $t1
lw $t3 8 
li $v0, 9
li $a0, 4
syscall
move $t2, $v0
sw $t3 $t2
sw $t2, $t1
lw $t6 b 
li $v0, 9
li $a0, 4
syscall
move $t7, $v0
sw $t6 $t7
lw $t6 8 
li $v0, 9
li $a0, 4
syscall
move $t4, $v0
sw $t6 $t4
lw $t6 8 
li $v0, 9
li $a0, 4
syscall
move $t5, $v0
sw $t6 $t5
add $t6, $t4, $t5
sw $t6, $t7
