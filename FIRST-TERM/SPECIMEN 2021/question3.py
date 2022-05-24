
QueueData = ['' for x in range(0,20)]
StartPointer = 0
EndPointer = 0

def Enqueue(QueueData, data):
    global EndPointer
    if EndPointer == 20:
        return False
        print('value not inserted')

    else:
        QueueData[EndPointer] = data
        EndPointer = EndPointer + 1
        return True



def ReadFile():
    filename = input('what is the filename?')
    if(os.path.isfile(filename)):
        f = open('filename', 'r')
        flag = True
        DataToInsert = (f.reafline()).strip()
        while(flag == True and DataToInsert != None):
            Flag, EndPointer = Enqueue(QueueData)
            DataToInsert = (f.readline()).strip()
            


