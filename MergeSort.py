def MergeSort(array):
    if len(array) <= 1:
        return array
    mid = (len(array)) // 2
    left = MergeSort(array[:mid])
    right = MergeSort(array[mid:])

    return Merge(left, right)
def Merge(left, right):
    left_index,right_index = 0,0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += right[right_index:]
    result += left[left_index:]
    return result   
myList = [54,26,93,17,77,31,44,55,20]
print(MergeSort(myList))