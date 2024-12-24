lw $t1 x 
li $v0, 9
li $a0, 4
syscall
move $t2, $v0
sw $t1 $t2
lw $t1 5 
li $v0, 9
li $a0, 4
syscall
move $t3, $v0
sw $t1 $t3
sw $t3, $t2
lw $t4 y 
li $v0, 9
li $a0, 4
syscall
move $t5, $v0
sw $t4 $t5
lw $t4 5 
li $v0, 9
li $a0, 4
syscall
move $t6, $v0
sw $t4 $t6
lw $t4 4 
li $v0, 9
li $a0, 4
syscall
move $t7, $v0
sw $t4 $t7
mul $t4, $t6, $t7
sw $t4, $t5
