size = 10
class Node:
    def __init__(self):
        self.data = ''
        self.left = None
        self.right = None


def initialisetree():
    global tree,rootpointer,freepointer

    tree = [Node() for x in range(size)]

    for i in range(size-1):

        tree[i].left = i+1 

    freepointer = 0



def addtotree(newdata):
    global tree,rootpointer,freepointer
    
    if freepointer is None:
        print('error - ',newdata, 'cannot be added, tree is full ')

    else:
        newpointer = freepointer
        tree[newpointer].data = newdata
        freepointer = tree[newpointer].left
        tree[newpointer].left = None

        if rootpointer is None:
            rootpointer = newpointer
            print('root pointer was set')

        else:
            pointer , direction = findinsertionpoint(newdata)

            if direction == 'left':
                tree[pointer].left = newpointer
            else:
                tree[pointer].right = newpointer


        print('added', newdata, 'to tree')



def findinsertionpoint(newdata):
    pointer = rootpointer

    while pointer is not None:

        prevpointer = pointer
        current = tree[pointer].data

        if current < newdata:
            direction = 'right'
            pointer = tree[pointer].right
        else:
            direction = 'left'
            pointer = tree[pointer].left

    return prevpointer, direction 



def traversetree(pointer = None):

    if rootpointer is None:
        print('cannot traverse, tree is empty')
        return

    if pointer is None:
        pointer = rootpointer

    left = tree[pointer].left
    right = tree[pointer].right
    data = tree[pointer].data

    if left is not None:
        traversetree(left)

    print(data)

    if right is not None:
        traversetree(right)



def searchtree(data):
    
    
    pointer = rootpointer
    
    search = True
    
    while search:

        current = tree[pointer].data

        if pointer is None:
            print('data not found')
            search = False
        
        
        if tree[pointer].data == data:
            print(data, 'was found at position', pointer)
            search = False
            
            current = tree[pointer].data

        elif current < data:
            direction = 'right'
            pointer = tree[pointer].right
        else:
            direction = 'left'
            pointer = tree[pointer].left



def test():
    global tree, freepointer,rootpointer

    initialisetree()
    addtotree('mouse')
    addtotree('cat')
    addtotree('dog')
    addtotree('horse')
    addtotree('sheep')
    addtotree('goat')
    addtotree('bat')
    addtotree('lizard')
    addtotree('lion')
    addtotree('tiger')
    addtotree('cheetah')
    addtotree('giraffe')

    traversetree()



if __name__ == '__main__':
    tree = []
    freepointer = None
    rootpointer  = None

    test()
    searchtree('tiger')
