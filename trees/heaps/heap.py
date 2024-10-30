input = [2,4,8,5,1,3,9,7]

def max_heapify(arr):
    # Turn an array into a max heap
    
        if i*2+1 < len(arr) and i*2+2 < len(arr):
            if arr[i] < arr[i*2+1]:
                temp = arr[i]
                arr[i], arr[i*2+1] = arr[i*2+1], temp
            if arr[i] < arr[i*2+2]:
                temp = arr[i]
                arr[i], arr[i*2+2] = arr[i*2+2], temp


max_heapify(input)
print(input)