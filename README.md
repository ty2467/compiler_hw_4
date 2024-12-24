name: Mike Yang  
uni: ty2467

Optimizations:
    Constant Folding  
    Constant Propagation  
    Strength Reduction  
    Copy Propagation  

Explanation:
optimize.py:
-file with all the optimization functions  
-constant folding; if there is an instruction with two constants, the computation gets performed in compile time  
-constant propagation: propagates the constant assigned to a variable  
-strength reduction: makes multiplication into addition for cheaper. note if the factor is too high then don't do it  
copy propagation: propagates a variable assignment  

these functions will get called by instruction_selection  

instruction_selection.py:  
same instruction selection algorithm from HW3. It takes a tree, and generates code. Now, before it generates code,
it first optimizes it.  
Of course only instruction_selection.py needs to run. instruction_selection calls the optimizing functions from optimize.py
and executes the optimization on them.  


node_class_4.py:  
four test cases, each an IR with their problem   
same constraint on hw3 persists, for both homeworks only can start from ast, not lexer or sc.




Video Link:  
https://drive.google.com/drive/u/0/home




Results notes:
Because the logging is still difficult to read, I have attached here the optimized results:
1. Constant folding,  
you will see that the code goes from 2+3 to 5    
log: pre optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=x, children=[]), Node(type=BinOp, value=+, children=[Node(type=Constant, value=2, children=[]), Node(type=Constant, value=3, children=[])])]), Node(type=Assign, value==, children=[Node(type=Name, value=y, children=[]), Node(type=BinOp, value=*, children=[Node(type=Name, value=x, children=[]), Node(type=Constant, value=4, children=[])])])])

log: optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=x, children=[]), Node(type=Constant, value=5, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=y, children=[]), Node(type=BinOp, value=*, children=[Node(type=Constant, value=5, children=[]), Node(type=Constant, value=4, children=[])])])]) 

2. Constant Propagating   
you will see that the code goes from operating on x + 3 to 5+3  
log: pre optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=x, children=[]), Node(type=Constant, value=5, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=y, children=[]), Node(type=BinOp, value=+, children=[Node(type=Name, value=x, children=[]), Node(type=Constant, value=3, children=[])])])]) 


log: optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=x, children=[]), Node(type=Constant, value=5, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=y, children=[]), Node(type=BinOp, value=+, children=[Node(type=Constant, value=5, children=[]), Node(type=Constant, value=3, children=[])])])]) 

3. Strength Reduction  
you will actually see two optimization here. The first is a constant folding turning  3 + 5 into 8, then you have the strength reduction   
log: pre optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=a, children=[]), Node(type=BinOp, value=+, children=[Node(type=Constant, value=5, children=[]), Node(type=Constant, value=3, children=[])])]), Node(type=Assign, value==, children=[Node(type=Name, value=b, children=[]), Node(type=BinOp, value=*, children=[Node(type=Name, value=a, children=[]), Node(type=Constant, value=2, children=[])])])]) 

log: optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=a, children=[]), Node(type=Constant, value=8, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=b, children=[]), Node(type=BinOp, value=+, children=[Node(type=Constant, value=8, children=[]), Node(type=Constant, value=8, children=[])])])])

4. Copy Propagation  
you will see that the variable a is propagated down to where it was b, as we assigned b = a.  

log: pre optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=b, children=[]), Node(type=Name, value=a, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=c, children=[]), Node(type=BinOp, value=+, children=[Node(type=Name, value=b, children=[]), Node(type=Constant, value=5, children=[])])])]) 

log: optimized tree: Node(type=Module, value=None, children=[Node(type=Assign, value==, children=[Node(type=Name, value=b, children=[]), Node(type=Name, value=a, children=[])]), Node(type=Assign, value==, children=[Node(type=Name, value=c, children=[]), Node(type=BinOp, value=+, children=[Node(type=Name, value=a, children=[]), Node(type=Constant, value=5, children=[])])])]) 

