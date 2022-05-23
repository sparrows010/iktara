class Picture:
    # __Description String
    # __Width Integer
    # __Height Integer
    # __FrameColour String
    
    def __init__(self,newDescription,newWidth,newHeight,newFrameColour):
        self.__Description = newDescription
        self.__Width  = newWidth
        self.__Height = newHeight
        self.__FrameColour = newFrameColour

    def GetDescription(self):
        return self.__Description
    
    def GetHeight(self):
        return self.__Height 

    def GetWidth(self):
        return self.__Width
    
    def  GetColour(self):
        return self.__FrameColour

    def SetDescription(self, newDescription):
        self.__Description = newDescription


PictureArray = [Picture('','','','') for x in range(0,100)]


def ReadData(PictureArray): 
    try:
        f = open('D:\Code projects\WINTER 2021\Pictures.txt', 'r')
        lines = f.readlines()
        descp = 1-1
        widthp = 2-1
        heightp = 3-1
        framep = 4-1
        count = 0

        for x in range(0,21):
            descT = lines[descp]
            widthT = lines[widthp]
            heightT = lines[heightp]
            frameT = lines[framep]

            descp = descp + 4
            widthp = widthp + 4
            heightp = heightp + 4
            framep = framep + 4
            count = count + 1

            PictureArray[count] = Picture(descT,widthT,heightT,frameT)

    except IOError():
        print('file not found')

    

ReadData(PictureArray)

frameco = str(input('input frame colour: ').lower())
maxwidth = int(input('enter maximum width: '))
maxheight = int(input('enter max height: '))


def findframe(PictureArray, frameco, maxwidth, maxheight):
    for x in range(1,22):
        if frameco == str(PictureArray[x].GetColour().strip()):
            if int(PictureArray[x].GetWidth()) <= maxwidth:
                if int(PictureArray[x].GetHeight()) <= maxheight:
                    print(PictureArray[x].GetDescription().strip(), '', PictureArray[x].GetWidth().strip(), PictureArray[x].GetHeight().strip())
            

findframe(PictureArray, frameco, maxwidth, maxheight)


            




