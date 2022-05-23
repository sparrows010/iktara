TheData = [20 ,3 ,4 ,8 ,12 ,99 ,4 ,26 ,4]

def InsertionSort(TheData):
    for Count in range(0,len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1

        while(NextValue >= 0 and Inserted != 1):
            if(DataToInsert < TheData[NextValue]):
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert
            else:
                Inserted = 1


def display(Thedata):
    for x in range(0,len(TheData)):
        print(TheData[x]) 


print('before sort : ', TheData)
InsertionSort(TheData)
print('after sort: ', TheData)

def checknum(TheData):
    userinp = int(input('Which number do we search?'))
    for x in range(0,len(TheData)):
        if TheData[x] == userinp:
            print('Value Found')
            return True
        
    else:
        print('Value Not Found')
        return False


checknum(TheData)
    