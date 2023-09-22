class Trees2:

    def __init__(self,key):
        
        self.key,self.left,self.right=key,None,None
    
    def height(self):

        if self is None:
            return 0
        else:
            return 1 + max(Trees2.height(self.left),Trees2.height(self.right))
        
    def size(self):

        if self is None:
            return 0
        else:
            return 1 + (Trees2.height(self.left),Trees2.height(self.right))
    
    def traverse(self):

        if self is None:
            return []
        else:
            return (Trees2.traverse(self.left)+ [self.key] +Trees2.traverse(self.right))
        
    def pt(data):

        if isinstance(data, tuple) and len(data)==3:

            node=Trees2(data[1])
            node.left=pt(data[0])
            node.right=pt(data[2])

        elif node is None:
            node = None
        else:
            node=Trees2(data)
        return node
    
tree=Trees2(((1,2,3),4,(5,6,7)))