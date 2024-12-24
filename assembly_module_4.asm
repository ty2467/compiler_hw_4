lw $t1 b 
li $v0, 9
li $a0, 4
syscall
move $t2, $v0
sw $t1 $t2
lw $t1 a 
li $v0, 9
li $a0, 4
syscall
move $t3, $v0
sw $t1 $t3
sw $t3, $t2
lw $t7 c 
li $v0, 9
li $a0, 4
syscall
move $t4, $v0
sw $t7 $t4
lw $t7 a 
li $v0, 9
li $a0, 4
syscall
move $t5, $v0
sw $t7 $t5
lw $t7 5 
li $v0, 9
li $a0, 4
syscall
move $t6, $v0
sw $t7 $t6
add $t7, $t5, $t6
sw $t7, $t4
