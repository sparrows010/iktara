arr = [213,323,5,324,12,352,123,644,223]   
arr.sort()

def bsearch(arr, l, r, target):
    while l<=r:
       mid = (l+r) // 2
   
       if arr[mid] == target:
           return True
   
       if target > arr[mid]:
           return bsearch(arr, mid+1, r, target)
           
       if target < arr[mid]:
           return bsearch(arr, l, mid-1, target)
   
    return -1

target = 323
print(bsearch(arr, 0, len(arr)-1, target))


"""
initialise array
SORT array
function for bsearch - params -- (arr, l , r , target val )
if target == mid, give true 
if target > mid 
recur but l == mid+1
if target < mid 
recur r == mid - 1
make target 
PRINT BSEARCH
"""
