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
        self.__LastFinds = [['' for x in range(0,2)] for j in range(0,10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation


TheBoxes = [HiddenBox('','','','') for x in range(0,10000)]
counter = -1

def NewBox(TheBoxes):
    global counter
    boxname = input('what is the box name? ')
    creatorname = input("what is the creator's name? ")
    datehidden = input('When was it hidden? ')
    gamelocat = input('where is the game location? ')

    TheBoxes[counter] = HiddenBox(boxname,creatorname,datehidden,gamelocat)
    counter = counter - 1

NewBox(TheBoxes)


class PuzzleBox(HiddenBox):
    # __PuzzleText String
    # __Solution String
    def __init__(self, NewBoxName, NewCreator, NewDateHidden, NewGameLocation, NewPuzzleText, NewSolution):
        super().__init__(self, NewBoxName, NewCreator, NewDateHidden, NewGameLocation)

        self.__PuzzleText = NewPuzzleText
        self.__Solution = NewSolution



