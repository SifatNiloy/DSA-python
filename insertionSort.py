# i=step 

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j-1
            
        array[j+1] = key
        

data = [9, 5, 1, 4, 3, 15, 21, 13, 8, -4, 0, 11, 15, -2]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)
