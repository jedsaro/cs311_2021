class Node:

    def __init__(self):
        
        self.children = []
        self.name = "taco"
        self.children_connection_weights = []

    def make_children(self, current_layer, nodes_per_layer_map):
        if current_layer == len(nodes_per_layer_map):
            return

        for i in range( nodes_per_layer_map[current_layer] ):
            self.children.append(Node())
            



    

    
        

