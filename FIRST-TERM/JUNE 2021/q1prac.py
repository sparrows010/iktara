class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8),node(56,3), node(0,9),node(0,-1)]
startPointer = 0
emptyList = 5

def outputNodes(linkedlist, CurrentPointer):
    while(CurrentPointer != -1):
        print(str(linkedlist[CurrentPointer].data))
        CurrentPointer = linkedlist[CurrentPointer].nextNode
        
def addNode(linkedList,CurrentPointer,emptyList):
    item = int(input('item to insert:'))
    if emptyList < 0 or emptyList > 9:
        return False

    else:
        newnode = node(item,-1)
        linkedList[emptyList] = newnode
        
        previouspointer = 0
        
        while CurrentPointer != -1:
            previouspointer = CurrentPointer
            CurrentPointer = linkedList[CurrentPointer].nextNode
        linkedList[previouspointer].nextNode = emptyList
        emptyList = linkedList[emptyList].nextNode

        return True


outputNodes(linkedList,0)
addNode(linkedList,0,5)
outputNodes(linkedList,0)
