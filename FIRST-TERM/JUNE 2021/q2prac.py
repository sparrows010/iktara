arrayData = [10 ,5 ,6 ,7 ,1 ,12 ,13 ,15 ,21 ,8]

def linearSearch(item, arrayData):
    for x in range(0,len(arrayData)):
        if arrayData[x] == item:
            return True
    else:
        return False

item = int(input('enter a value to search:'))
output = linearSearch(item, arrayData)
if output == True:
    print('value was found')
else:
    print('value not found')


def bubbleSort(theArray):
    for x in range(0,10):
        for y in range(0,9):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp 

