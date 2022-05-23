class node():
   def __init__(self, dataval = None):
       self.dataval = dataval 
       self.nextval = None

class linklist():
    def __init__(self ,headval = None):
        self.headval = headval

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def atbegg(self, newnode):
        newnode = node(newnode)
        newnode.nextval = self.headval 
        self.headval = newnode
    
    def at_end(self, newdata):
      NewNode = node(newdata)
      if self.headval is None:
         self.headval = NewNode
         return
      laste = self.headval
      while(laste.nextval):
         laste = laste.nextval
      laste.nextval=NewNode

list = linklist()
list.headval = node('sun')
e2 = node('mon')
e3 = node('tue')
list.headval.nextval = e2
e2.nextval = e3
list.atbegg('sex')
list.at_end("Thu")


list.printlist()


