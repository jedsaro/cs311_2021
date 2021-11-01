import java.io.*;
import java.util.ArrayList;
//import java.util.Iterator;

public class Agent {

    public static void main(String[] args) throws IOException {

        Agent evilme = new Agent();
        ArrayList<String> list = new ArrayList<>();

        list = evilme.filetoArray();

        evilme.run(args, list);

    }

    // =======================================================

    public void run(String [] args, ArrayList<String> list) {

        double percentageC = getConfessions(list)/list.size();
        
        inputReader(args);

        if(percentageC > 0.3)
        {
            alwaysSilent();
            
        }
        else
        {
            alwaysConfess();
        }

    }

    public void alwaysConfess() 
    {
        System.out.println("confess");
    }

    public void alwaysSilent()
    {
        System.out.println("silent");
    }

    // =============================================================================================
    // tools

    public double getSilent(ArrayList <String>  methodArray) {

        double total = 0;

        for (int i = 0; i < methodArray.size(); i++) {
            if (methodArray.get(i).equals("silent")) {
                total++;

            }
        }

        return total;
    }

    public double getConfessions(ArrayList <String> methodArray) {

        double total = 0;

        for (int i = 0; i < methodArray.size(); i++) {
            if (methodArray.get(i).equals("confess")) {
                total++;

            }
        }

        return total;
    }

    // reads txt file and places it into an array
    public ArrayList<String> filetoArray() throws IOException {

        BufferedReader readtext = new BufferedReader(new FileReader("Enemy_Input.txt"));

        String str;

        ArrayList<String> enemyInput = new ArrayList<String>();

        while ((str = readtext.readLine()) != null) {

            enemyInput.add(str);
        }

        return enemyInput;
    }

    // reads user input and stores it into a txt file
    public void inputReader(String[] args) {

        try {

            BufferedWriter file = new BufferedWriter(new FileWriter("Enemy_Input.txt", true));
            String val = args[0];
            file.write(val);
            file.newLine();
            file.close();

            System.out.print(args[0]);

        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }

}
