class TreasureChest:
    # __question : String
    # __answer : Integer
    # __points : Integer
    def __init__(self, question, answer, points):
        self.__question = question
        self.__answer = answer
        self.__points = points
    def getQuestion(self):
        return self.__question 
    def checkAnswer(self, answer):
        if int(self.__answer) == answer:
            return True
        else:
            return False
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return int(self.__points)//2        # the "//" returns an interger value after div whereas "/" returns float #
        elif (attempts == 3 or attempts == 4):
            return int(self.__points)//4
        else:
            return 0


arrayTreasure = []

def readData():
    global arrayTreasure
    f = open("D:\Code projects\JUNE 2021\TreasureChestData.txt","r")
    lines=f.readlines()
    try:
        quesP = 1 - 1
        ansP = 2-1
        poiP = 3-1
        
        
        for x in range(0,5):
            
            question = (lines[quesP])
            quesP = quesP + 3
            print(question)
            answer = (lines[ansP])
            ansP = ansP + 3
            print(answer)
            points = (lines[poiP])
            poiP = poiP + 3
            print(points)
            
            
            arrayTreasure.append(TreasureChest(question,answer,points))

        
    except IOError:
        print("Could not find file")

readData()



choice = int(input('which treasure chest to open: '))
if choice > 0 and choice < 6:
    flag = False
    attempts = 0
    while flag == False:
        print(arrayTreasure[choice-1].getQuestion())
        userans = int(input('enter answer: '))
        flag = arrayTreasure[choice -1].checkAnswer(userans)
        attempts = attempts + 1
pointsearned = arrayTreasure[choice - 1].getPoints(attempts)
print('Points earned:', pointsearned)




