class HiddenBox:
    # __BoxName String
    # __Creator String
    # __DateHidden String
    # __GameLocation String
    # __LastFinds [10][2] String
    # __Active String
     
     def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewGameLocation):
         self.__BoxName = NewBoxName
         self.__Creator = NewCreator
         self.__DateHidden = NewDateHidden
         self.__GameLocation = NewGameLocation
         self.__LastFinds = [['' for j in range(0,2)] for i in range(0,10)]
         self.__Active = False

    
     def GetBoxName(self):
         return self.__BoxName

     def GetGameLocation(self):
         return self.__GameLocation
          

TheBoxes = [HiddenBox('','','','') for j in range(0,10000)]


def NewBox(TheBoxes, NumBoxes):
    NewBoxName = input('What is the Boxes name? ')
    NewCreator = input('what is the creator name? ')
    NewDateHidden = input('what is the date? ')
    NewGameLocation = input('where is the game location? ')

    TheBoxes[NumBoxes]= HiddenBox(NewBoxName,NewCreator,NewDateHidden,NewGameLocation)
    return(NumBoxes + 1)

NumBoxes = NewBox(TheBoxes, -1)


class PuzzleBox(HiddenBox):
    # __PuzzleText String
    # __Solution String
    
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewGameLocation, NewPuzzleText, NewSolution):
        super().__init__(NewBoxName, NewCreator, NewDateHidden, NewGameLocation)
        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution
        