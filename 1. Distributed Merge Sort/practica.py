import random

arr = []


for i in range(0, 8):
    arr.append(random.randint(0, 1000))

print(arr)


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    arr1 = arr[: len(arr) // 2]
    arr2 = arr[len(arr) // 2:]
    print(arr1)
    print(arr2)
    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)    

    if arr1 is not None and arr2 is not None:
        sortedSubArr = []
        lenArr1 = len(arr1)
        lenArr2 = len(arr2)

        for i in range(0, max(lenArr1, lenArr2)):
            if arr1[i] > arr2[i]:
                sortedSubArr.append(arr2[i])
                arr2.remove(arr2[i])
            else:
                sortedSubArr.append(arr1[i])
                arr1.remove(arr1[i])
        print(f'-------------------- {sortedSubArr}')
        


    # sortedSubArr = []
    # print('Merge Arrays -----------')
    # print(arr1)
    # print(arr2)
    
    # if arr1[0] > arr2[0]:
    #     sortedSubArr.append(arr2[0])
    #     arr2.remove(arr2[0])
    # else:
    #     sortedSubArr.append(arr1[0])
    #     arr1.remove(arr1[0])
    
    # while len(arr1) != 0:
    #     sortedSubArr.append(arr1[0])
    #     arr1.remove(arr1[0])
    # while len(arr2) != 0:
    #     sortedSubArr.append(arr2[0])
    #     arr2.remove(arr2[0])

    # print(f'Arreglo ordenado {sortedSubArr}')
    

mergeSort(arr)