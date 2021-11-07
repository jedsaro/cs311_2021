class Node:

    def __init__(self):
        
        self.children = []
        self.node_name = "taco"
        self.children_connection_weights = []

    def make_children(self, current_layer, nodes_per_layer_map):
        

