import random
import simpy
import math

class Node:
    def __init__(self, value):
        self.value = value # Node value (arr)
        self.children = 0 # Number of Node's childrens (int) = expected messages
        self.parent = None # Node's parent (arr)

class Tree: 
    def __init__(self, env, root_value = None):
        self.env = env
        self.root_value = Node(root_value) if root_value is not None else None
        self.root_children = 2 if len(self.root_value.value) != 1 else 0

    def generateNodes(self, node):
        if len(node.value) == 1:
            print(f'Leaf node reached: {node.value}')
            return

        if node.value == self.root_value.value:
            print('-------------------- ROOT NODE --------------------')
            print(node.value)

        arr = node.value
        leftArr  = arr[ : len(arr) // 2]
        rightArr = arr[len(arr) // 2 : ]

        leftNode = Node(leftArr)
        rightNode = Node(rightArr)

        rightNode.parent, leftNode.parent = node, node
        
        try:
            leftNode.children = len(leftArr) // math.ceil(len(leftArr) // 2)
            rightNode.children = len(rightArr) // math.ceil(len(rightArr) // 2)
        except:
            leftNode.children, rightNode.children = 0, 0

        print('------------------------------------------------------------------------------')
        print(f'Environment Time: {self.env.now} - Splitting {node.value} -> {leftNode.value} & {rightNode.value}')

        yield env.timeout(1)
        # para los procesos de abajo no usamos yield porque queremos que comiencen al mismo tiempo y uno no espere al otro para comenzar
        left_process = self.env.process(self.generateNodes(leftNode))
        right_process = self.env.process(self.generateNodes(rightNode))
        yield left_process & right_process # esperamos a que ambos procesos hayan terminado antes de continuar con la ejecución del código

        merged_message = self.merge_messages(leftNode.value, rightNode.value)
        node.value = merged_message
        print('------------------------------------------------------------------------------')
        print(f'Environment Time: {self.env.now} - Merging: {leftNode.value} & {rightNode.value} -> {merged_message}')
        yield env.timeout(1)


    def merge_messages(self, message1, message2):
        merged = []
        i, j = 0, 0

        while i < len(message1) and j < len(message2):
            if message1[i] < message2[j]:
                merged.append(message1[i])
                i += 1
            else:
                merged.append(message2[j])
                j += 1

        for elem in message1[i:]:
            merged.append(elem)
        for elem in message2[j:]:
            merged.append(elem)

        return merged


# Simpy enviroment
env = simpy.Environment()

# Random Array
arr = [random.randint(0, 1000) for _ in range(8)]

# Tree instantiation and process initialization
arbol = Tree(env, arr)
env.process(arbol.generateNodes(arbol.root_value))

# Simulation Execution
env.run()