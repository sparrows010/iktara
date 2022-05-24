def ReadFile(QueueData, StartP, EndP):
    filename = input('Enter filename: ')
    if(os.path.ispath(filename)):
        f = open(filename, 'r')
        flag = True
        DataToInsert = (f.readline()).strip()
        while(flag == True and DataToInsert != None):
            flag, EndP = Enqueue(QueueData, EndP)
            DataToInsert = (f.readline()).strip()
        if flag == False:
            f.close()
            return  1, EndP
        else:
            f.close()
            return 2, EndP
    else:
        return -1, EndP

ReturnValue, EndP = ReadFile(QueueData, StartP, EndP)
if ReturnValue == 1:
    print('all data was succesfully stored')
elif ReturnValue == 2:
    print('the array is full')
elif ReturnValue == -1:
    print('file not found')
