import java.util.ArrayList;
import java.util.List;

class Node{

public List <Node> children;
public List <Double> weight;
String name;

    public Node()
    {
        this.children = new ArrayList<Node>();
        this.weight = new ArrayList<Double>();
        this.name = "taco";
    }   

    public void make_children(int current_layer, ArrayList<Integer> nodes_per_layer)
    {
        if (current_layer >= nodes_per_layer.size())
        {
            return;
        }

        for(int i = 1;  i < nodes_per_layer.get(current_layer); i++)
        {
            this.children.add(new Node());
        }

        this.children.get(0).make_children(current_layer++ , nodes_per_layer);

        for(int i = 1;  i < nodes_per_layer.size(); i++)
        {
            this.children.get(i).children = this.children.get(0);
        }

    }
    
    public static void main(String[] args) {

        ArrayList<Integer> GLOBAL_MAP = new ArrayList<Integer>(){
            {
                add(4);
                add(3);
                add(2);
            }
        };



        Node node = new Node();
        node.make_children(0, GLOBAL_MAP);



        /* node.print(0, GLOBAL_MAP);

        System.out.println("After: ");

        node.random_weights(0, GLOBAL_MAP);
        node.print(0, GLOBAL_MAP);
 */
    }




}




