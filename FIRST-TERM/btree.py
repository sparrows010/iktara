class Node:
    def __init__(self,data):
        self.leftc = None
        self.rightc = None 
        self.data = data

def insertbtree(root, node):
    if root == None:
        root = node

    else:
        if root.data > node.data:
            if root.leftc == None:
                root.leftc = node
            else:
                insertbtree(root.leftc, node)
        else:
            if root.rightc == None:
                root.rightc = node

            else:
                insertbtree(root.rightc, node)


def inorder(root):
    if root is None:
        return 
    else:
        inorder(root.leftc)
        print(root.data)
        inorder(root.rightc)

def preorder(root):
    if root is None:
        return
    else:
        print(root.data)
        preorder(root.leftc)
        preorder(root.rightc)


def postorder(root):
    if root is None:
        return
    else:
        postorder(root.leftc)
        postorder(root.rightc)
        print(root.data)




r = Node(3)
insertbtree(r, Node(7))
insertbtree(r, Node(1))
insertbtree(r, Node(5))

print(postorder(r))

