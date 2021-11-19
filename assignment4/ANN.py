import random

NODE_COUNT_PER_LAYER =  [4,3,2]

class Node:
    def __init__(self, name):
        
        self.children = [] 
        self.weight = []
        self.name = name

    def make_children(self, current_layer_number, nodes_per_layer_map):

        if current_layer_number >= len(nodes_per_layer_map):
            return

        for i in range(nodes_per_layer_map[current_layer_number]):

            self.children.append(Node(chr(ord(self.name) + 1)))

        #recursion
        self.children[0].make_children(current_layer_number + 1 , nodes_per_layer_map)

        for i in range(1, len(self.children)):
            self.children[i].children = self.children[0].children[:]


    def prety_print(self, current_layer_number, node_per_layer_map):
        
        indent = '   ' * current_layer_number #output organizor

        if current_layer_number >= len(node_per_layer_map):

            print(f"{indent} {self.name}")
            return 

        print(f"{indent} {self.name} is connected to: ")

        for i in range(len(self.children)):
            try: 

                print(f"{indent} Weight of {self.weight[i]}")

            except:
                pass

            self.children[i].prety_print(current_layer_number + 1, node_per_layer_map)

        return 

    def set_random_weights(self, current_layer_number, node_per_layer_map):
        if current_layer_number >= len(node_per_layer_map):
            return

        self.weight = [0.0] * len(self.children)

        for i in range(len(self.children)):

            self.weight[i] = random.uniform(0, 1)

            self.children[i].set_random_weights(current_layer_number + 1, node_per_layer_map)

        return


if __name__ == '__main__':

    node = Node("A")
    node.make_children(0, NODE_COUNT_PER_LAYER)
    node.prety_print(0, NODE_COUNT_PER_LAYER)

    print("After: ")

    node.set_random_weights(0, NODE_COUNT_PER_LAYER)
    node.prety_print(0, NODE_COUNT_PER_LAYER)







        

    

    
        

