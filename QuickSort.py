"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array, low, high):
    if(low < high):
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi +1, high)

    return array
def partition(array, low, high):
    pivot = array[high]
    #left hand side of array index
    i = low - 1
    for j in range(low, high):
        if(array[j] < pivot):
            i += 1
            array[i], array[j] = array[j],array[i]
    array[i + 1], array[high] = array[high], array[i+1]
    return i + 1

    
test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print(quicksort(test, 0 , len(test) - 1))