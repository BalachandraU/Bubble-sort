def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):

       
        swapped = False
        for j in range(0, n-i-1):

            
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            
            return



arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

