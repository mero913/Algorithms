#This function sort array from low to high value

def FindSmallest(arr):

    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

#print(FindeSmallest(my_arr))

def selectionSort(arr):

    newArr = []
    
    for i  in range(len(arr)):
        smallest = FindSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

print(selectionSort([3, 1, 4, 7, 2]))

