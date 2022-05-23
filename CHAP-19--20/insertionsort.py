arr = [213,323,5,324,12,352,123,644,223]   

def inssort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        while i > 0 and temp < arr[i-1]:
            arr[i] = arr[i-1]
            i = i-1
       
        arr[i] = temp


inssort(arr)
print(arr)


'''
make arr
def 
i in range 1 to len(arr)
make temp = arr i 
while i > 0 AND temp < arr[i-1]
switch em 
arr[i] = arr[i-1]
decrement i
i= i - 1
make arr[i] = temp 
out of while loop  
'''
