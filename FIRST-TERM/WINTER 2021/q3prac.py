ArrayNodes = [[0 for i in range(0, 3)] for j in range(0,20)] #each of the 20 nodes have a root node and a left & right pointer
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Enter the data"))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1            #20 rows and 3 colomns
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1  
        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def PrintAll(ArrayNodes):
    for x in range(0,20):
        print(ArrayNodes[x][0], '  ', ArrayNodes[x][1], '  ', ArrayNodes[x][2])

for x in range(0,10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)


PrintAll(ArrayNodes)

def InOrder(ArrayNodes,RootNode):
    if ArrayNodes[RootNode][0] != -1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][0])
    print(str(ArrayNodes[RootNode][1]))
    if ArrayNodes[RootNode][2] != -1:
        InOrder(ArrayNodes,ArrayNodes[RootNode][2])

InOrder(ArrayNodes,-1)