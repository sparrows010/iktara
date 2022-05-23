import os


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

def display(TheData):
    for x in range(0,len(TheData)):
        print(TheData[x])

print('Beforesort:')
display(TheData)
print('After sort')
InsertionSort(TheData)
print(TheData)


def search(TheData):
    userinp = int(input('enter number to search: '))
    for x in range(0,len(TheData)):
        if(TheData[x] == userinp):
            print('Value Found')
            return True
    else:
        print('Value not found ')
        return False


search(TheData)
search(TheData) 



class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active [String]
    def __init__(self, BoxName,Creator,DateHidden,GameLocation):
        self.__BoxName = BoxName
        self.__Creator = Creator
        self.__DateHidden = DateHidden
        self.__GameLocation = GameLocation
        self.__LastFinds = [['' for x in range(0,2)] for i in range(0,10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation

    
TheBoxes = [HiddenBox('','','','') for x in range(0,10000)]


def NewBox(TheBoxes, NumBoxes):
    NewBoxName = input('enter box name: ')
    NewCreator = input('enter creator name: ')
    NewDateHidden = input('enter Date: ')
    NewGameLocation = input('enter game location: ')
    
    TheBoxes[NumBoxes] = HiddenBox(NewBoxName,NewCreator,NewDateHidden,NewGameLocation)
    return(NumBoxes + 1)

    NumBoxes = NewBox(TheBoxes, NumBoxes)
    
class PuzzleBox(HiddenBox):
    # __PuzzleText String
    # __Solution String
    def __init__(self, BoxName, Creator, DateHidden, GameLocation, NewPuzzleText, NewSolution):
        super().__init__(BoxName, Creator, DateHidden, GameLocation)

        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution


QueueData = ['' for x in range(0,20)]
StartP = 0
EndP = 0

def Enqueue(QueueData, StartP, EndP, Data):
    if EndP == 20:
        return False, EndP
    else: 
        QueueData[EndP] = Data
        EndP = EndP + 1
        return True, EndP
        
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






        

