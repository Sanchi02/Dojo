class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val
        
class BinTree:

    def __init__(self):
        self.root = None
        
    def insertRecursive(self, root, val):
        if(root.val < val):
            if(root.left!=None):
                self.insertRecursive(root.left, val)
            else:
                root.left = Node(val)
        else:
            if(root.right!=None):
                self.insertRecursive(root.right, val)
            else:
                root.right = Node(val)
            
        
    def insert(self,val):
        if(self.root==None):
            self.root = Node(val)
        else:
            self.insertRecursive(self.root,val)
    
    def printTree(self, root):
        print(root.val)
        if(root.left!=None):
            print("The root is {}, left child is {}".format(root.val,root.left.val))
            self.printTree(root.left)
        if(root.right!=None):
            print("The root is {}, right child is {}".format(root.val, root.right.val))
            self.printTree(root.right)
                      
treee = BinTree()

treee.insert(4)
treee.insert(5)
treee.insert(1)
treee.insert(2)
treee.insert(3)
treee.insert(6)
treee.insert(7)

treee.printTree(treee.root)
            