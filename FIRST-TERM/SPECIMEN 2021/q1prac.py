TheData = [20 ,3 ,4 ,8 ,12 ,99 ,4 ,26 ,4]

def InsertionSort(TheData):
    for count in range(0,len(TheData)):
        DataToInsert = TheData[count]
        Inserted = 0 
        NextValue = count - 1
        while(NextValue >= 0 and Inserted != 1): 
            if (DataToInsert < TheData[NextValue]):
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] = DataToInsert

            else:
                Inserted = 1

            
        
def display(TheData):
    for x in range(0,len(TheData)):
        print(TheData[x])

print('Array before sorting:')
display(TheData)
print('Array after sorting:')
InsertionSort(TheData)
print(TheData)


def search(TheData):
    userinp = int(input('enter a number to search:'))
    for x in range(0,len(TheData)):
        if TheData[x] == userinp:
            print('Value Found')
            return True

    else:
        print('Value Not found')
        return False

search(TheData)
search(TheData)