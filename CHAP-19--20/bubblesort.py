arr = [213,323,5,324,12,352,123,644,223]   
print(arr)
def bubblesort(arr):
    
    swap = True
    top = len(arr)
    
    while swap or top > 0:
        swap = False
        for i in range(top-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swap = True
        top = top - 1
        

bubblesort(arr)
print(arr)

"""
make array
func bubble sort
swap = true and top is len of arr
while swap or true > 0
swap = False
i in range of of top -1 
if arr i > arr i + 1
set temp to arr i
arr i = arr i + 1
arr i + 1 = temp
swap = true 
top = top -1 out of loop 
print arr
"""
