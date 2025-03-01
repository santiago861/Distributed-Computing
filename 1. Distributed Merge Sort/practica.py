import random

arr = []


for i in range(0, 16):
    arr.append(random.randint(0, 1000))

print(f'ARRAY INICIAL: {arr}')


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    
    # divide
    arr1 = arr[: len(arr) // 2]
    arr2 = arr[len(arr) // 2:]

    # recursion
    mergeSort(arr1)
    mergeSort(arr2)
    print(f'Arrays a ordenar: {arr1} - {arr2}')

    # # merge 
    i = 0 # left arr index
    j = 0 # right arr index 
    k = 0 # merged arr index

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1
    
    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1
    
    print('Resultado ----------------------------')
    print(arr)
    


mergeSort(arr)