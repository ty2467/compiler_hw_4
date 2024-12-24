lw $t2 x 
li $v0, 9
li $a0, 4
syscall
move $t3, $v0
sw $t2 $t3
lw $t2 5 
li $v0, 9
li $a0, 4
syscall
move $t1, $v0
sw $t2 $t1
sw $t1, $t3
lw $t5 y 
li $v0, 9
li $a0, 4
syscall
move $t6, $v0
sw $t5 $t6
lw $t5 5 
li $v0, 9
li $a0, 4
syscall
move $t7, $v0
sw $t5 $t7
lw $t5 3 
li $v0, 9
li $a0, 4
syscall
move $t4, $v0
sw $t5 $t4
add $t5, $t7, $t4
sw $t5, $t6
