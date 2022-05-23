arr = [213,323,5,324,12,352,123,644,223]   
item = int(input('enter a number to find: '))
found = False

for i in range(len(arr)):
    if(arr[i] == item):
        found = True
        print('found at index', i)
    
if found == False:
    print('not found')



#initialise array
#set found = false 
#write range for i in range of len of list
#if i == item 
#found  = true , print at index i
#if found == false, print not found

