import random

GLOBAL_MAP =  [4,3,2]

class Node:

    def __init__(self, name):
        
        self.children = [] 
        self.weight = []
        self.name = name

    def make_children(self, current_layer, nodes_per_layer):

        #last node terminates child creation
        if current_layer >= len(nodes_per_layer):
            return

        #populates nodes per layer and sends increment of char (recursion)
        for i in range(nodes_per_layer[current_layer]):

            self.children.append(Node(chr(ord(self.name) + 1)))

        #moves to next layer and 
        self.children[0].make_children(current_layer + 1 , nodes_per_layer)

        for i in range(1, len(self.children)):

            self.children[i].children = self.children[0].children[:]


    #function output
    def print(self, current_layer, node_per_layer):
        
        indent = '   ' * current_layer 

        if current_layer >= len(node_per_layer):

            print(f"{indent} {self.name}")
            return 

        print(f"{indent} {self.name} is connected to: ")

        for i in range(len(self.children)):
            try: 

                print(f"{indent} Weight of {self.weight[i]}")

            except:
                pass

            self.children[i].print(current_layer + 1, node_per_layer)

        return 

    def random_weights(self, current_layer, node_per_layer):

        #last node terminates weight creation
        if current_layer >= len(node_per_layer):
            return

        self.weight = [0.0] * len(self.children)

        for i in range(len(self.children)):

            #storing random numbers between 0 and 1
            self.weight[i] = random.uniform(0, 1)

            self.children[i].random_weights(current_layer + 1, node_per_layer)

        return


if __name__ == '__main__':

    node = Node("A")
    node.make_children(0, GLOBAL_MAP)
    node.print(0, GLOBAL_MAP)

    print("After: ")

    node.random_weights(0, GLOBAL_MAP)
    node.print(0, GLOBAL_MAP)







        

    

    
        

