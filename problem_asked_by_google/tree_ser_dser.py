class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def serialize(n=Node()):
    if(n==None):
        return
    serialize(n.left)
    print(n.val)
    serialize(n.right)

node = Node('root', Node('left', Node('left.left')), Node('right'))
serialize(node)