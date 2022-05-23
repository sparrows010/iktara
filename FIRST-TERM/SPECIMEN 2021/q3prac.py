
QueueData = ['' for x in range(0,20)]
StartPointer = 0
EndPointer = 0 

def Enqueue(data,QueueData,EndPointer):
    if EndPointer == 20:
        return False, EndPointer
    else:
        QueueData[EndPointer] = data
        EndPointer = EndPointer + 1
        return True, EndPointer

def ReadFile(QueueData, EndPointer):
    import os
    file = str(input('what is the filename? '))
    if os.path.isfile(file) == True:
        f = open(file, 'r')
        data = f.readline().strip()
        flag = True
        while flag == True and data != None:
            flag, EndPointer = Enqueue(data,QueueData,EndPointer)
            data = f.readline().strip()
        if flag == False and data == '':
            f.close
            return 1, EndPointer
        else:
            f.close
            return 2, EndPointer
    else:
        return -1, EndPointer


output, EndPointer = ReadFile(QueueData, EndPointer)
if output == 1 :
    print('all data was successfully added')
elif output == 2 :
    print('Queue is full')
elif output == -1:
    print('File not found')

def Remove(QueueData, StartPointer,EndPointer):
    if EndPointer - StartPointer < 2:
        return 'not enough items in queue', EndPointer, StartPointer
    else:
        val1 = QueueData[StartPointer]
        StartPointer = StartPointer + 1
        val2 =  QueueData[StartPointer]
        StartPointer = StartPointer + 1 
        print(val1 + ' ' + val2) 

        
Remove(QueueData,0,0)