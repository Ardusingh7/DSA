#STRUCTURE OF A TREE

class Tree:

    def __init__(self,key):
        
        self.key=key
        self.left=None
        self.right=None

def pt(data):
    
    if isinstance(data,tuple) and len(data)==3:

        node=Tree(data[1])
        node.left=pt(data[0])
        node.right=pt(data[2])
    elif data is None:
        node=None
    else:
        node=Tree(data)
    return node

def height(node):

    if node is None:
        return 0
    else:
        return 1+ max(height(node.left),height(node.right))
    
def sz(node):

    if node is None:
        return 0
    else:
        return 1+ sz(node.left),sz(node.right)
    
#TREE IS AN OBJ HERE 

Tree1=pt(((1,3),2,((4,5),6,(7,8))))

#print(Tree1.key)
#print(Tree1.left.key)
#print(Tree1.right.key)

print(height(Tree1))
#print(sz(Tree1))
