class TreasureChest:
    # __question string
    # __answer integer
    # __points integer

    def __init__(self,newquestion,newanswer,newpoints):
        self.__question = newquestion
        self.__answer = newanswer
        self.__points = newpoints

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, newanswer):
        if newanswer == self.__answer:
            return True
        else:
            return False
    
    def getPoints(self, attempts):
        if attempts == 1:
            return int(self.__points)
        elif attempts == 2:
            return  int(self.__points)//2
        elif attempts == 3 or 4:
            return int(self.__points)//4
        else:
            return 0








arrayTreasure = [TreasureChest('','','')]

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



choice = int(input("Enter question number of choice: "))
if (choice > 0 and choice < 6):
    flag = False
    attempts = 0
    while flag == False:
        print(arrayTreasure[choice - 1].getQuestion())
        userans = int(input("Enter answer: "))
        flag = arrayTreasure[choice - 1].checkAnswer(userans)
        attempts = attempts + 1
    pointearned = arrayTreasure[choice - 1].getPoints(attempts)
    print("Point earned: ", pointearned)


choice = int(input("Enter question number of choice: "))
if (choice > 0 and choice < 6):
    flag = False
    attempts = 0
    while flag == False:
        print(arrayTreasure[choice - 1].getQuestion())
        userans = int(input("Enter answer: "))
        flag = arrayTreasure[choice - 1].checkAnswer(userans)
        attempts = attempts + 1
    pointearned = arrayTreasure[choice - 1].getPoints(attempts)
    print("Point earned: ", pointearned)