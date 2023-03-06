def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i]==x):
            return i
    return -1


array=[2, 5, 8 ,23, 3, 15, 18]
n=len(array)
x=5
result= linearSearch (array, n, x)
if (result==-1):
    print("Element not found")
else:
    print("Element found at index", result)