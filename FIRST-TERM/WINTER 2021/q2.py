from turtle import width


class Picture:
    # __Description   INTEGER
    # __Width   INTEGER
    # __Height   INTEGER
    # __FrameColour   STRING

    def __init__(self, NewDescription, NewWidth, NewHeight, NewFrameColour):
        self.__Description = NewDescription
        self.__Width = NewWidth
        self.__Height = NewHeight
        self.__FrameColour = NewFrameColour

    def GetDescription(self):
        return self.__Description

    def GetWidth(self):
        return self.__Width

    def GetHeight(self):
        return self.__Height

    def GetFrameColour(self):
        return self.__FrameColour

    def SetDescription(self, NewDescription):
        self.__Description = NewDescription
    
PictureArray = [(Picture('',0,0,'')) for i in range(0,100)] 


def ReadData():
    f = open('D:\Code projects\WINTER 2021\Pictures.txt', 'r')
    lines = f.readlines()
    try:
        descp = 1-1
        widthp = 2-1
        heightp = 3-1
        colorp = 4-1
        picp = 0

        for x in range(0,21):
            desc = lines[descp]
            width = lines[widthp]     
            height = lines[heightp]
            color = lines[colorp]
            PictureArray.append(Picture(desc,width,height,color))

            descp = descp + 4
            widthp = widthp + 4
            heightp = heightp + 4
            colorp = colorp + 4
            picp = picp + 1


            
        f.close()
    
    
        
    
    except IOError:
        print('file is not found dumbass')
    
    print('Number of Pictures is :' ,picp)
        
ReadData()


userframe = input('what is the frame color? ').lower()
userheight = int(input('what is the height? '))
userwidth = int(input('what is the width? '))

for x in range(0,100):
    if PictureArray[x].FrameColour() == userframe:  
        if  PictureArray[x].Height() <= userheight: 
            if PictureArray[x].Width()  <= userwidth:
                print(PictureArray[x].Description())




