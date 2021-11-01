import java.util.Stack;

public class Agent {

    public static void main(String[] args) {

        Stack<String> stack = new Stack<String>();

        args = new String[1];
        
        stack.push("silent");
        stack.push("confess");

        if(args[0] == "silent")
        {
            System.out.println(stack.peek());
        }
        else
        {
            System.out.println(stack.pop());
        }

    }

}
