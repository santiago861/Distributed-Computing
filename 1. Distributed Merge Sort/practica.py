import random
import simpy
import math

env = simpy.Environment() # The first thing we need to do is to create an instance of Environment, this instance is passed into our process function
arr = []

for i in range(0, 8):
    arr.append(random.randint(0, 1000))


class Node:
    def __init__(self, value):
        self.value = value # Node value (arr)
        self.children = 0 # Number of Node's childrens (int)
        self.parent = None # Node's parent (arr)

    def go():
        pass
    
    def back():
        pass

class Tree:
    def __init__(self, root_value = None):
        self.root_value = Node(root_value) if root_value is not None else None
        self.root_children = len(root_value) // (len(root_value) // 2)

        self.root_value.value = root_value

    def generateNodes(self, arr):
        if len(arr) == 1:
            return Node(arr)
        elif arr == None:
            return 'Empty array passed'
        else:
            if arr == self.root_value.value:
                print(f'---------------- ROOT NODE VALUE ----------------')
                print(arr)

            left = arr[ : len(arr) // 2]
            right = arr[len(arr) // 2 : ]

            leftNode = Node(left)
            leftNode.value = left

            rightNode = Node(right)
            rightNode.value = right

            leftArr = left
            rightArr = right

            rightNode.parent = arr
            leftNode.parent = arr

            try:
                leftNode.children = len(leftArr) // math.ceil(len(leftArr) // 2)
                rightNode.children = len(rightArr) // math.ceil(len(rightArr) // 2)
            except:
                leftNode.children = 0
                rightNode.children = 0
            
            print(f'-------------------- CHILDRENS --------------------')
            print(leftNode.value)
            print(rightNode.value)
            
            self.generateNodes(leftArr)
            self.generateNodes(rightArr)

arbol = Tree(arr)
arbol.generateNodes(arr)
            
            






# def mergeSort(arr):
    # if len(arr) == 1:
    #     return arr 
    # # divide
    # arr1 = arr[: len(arr) // 2]
    # arr2 = arr[len(arr) // 2:]
    
    # # recursion
    # mergeSort(arr1)
    # mergeSort(arr2)
    # print(f'Arrays a ordenar: {arr1} - {arr2}')
    
    # # # merge 
    # i = 0 # left arr index
    # j = 0 # right arr index 
    # k = 0 # merged arr index
    # while i < len(arr1) and j < len(arr2):
    #     if arr1[i] < arr2[j]:
    #         arr[k] = arr1[i]
    #         i += 1
    #     else:
    #         arr[k] = arr2[j]
    #         j += 1
    #     k += 1
    # while i < len(arr1):
    #     arr[k] = arr1[i]
    #     i += 1
    #     k += 1
    # while j < len(arr2):
    #     arr[k] = arr2[j]
    #     j += 1
    #     k += 1
    # print('Resultado ----------------------------')
    # print(arr)
    


# mergeSort(arr)