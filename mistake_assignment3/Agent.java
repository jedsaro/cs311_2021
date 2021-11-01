import java.io.*;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Scanner;

public class Agent {

    public static void main(String[] args) throws IOException {

        Agent evilme = new Agent();
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();

        list = evilme.filetoArray();

        evilme.run(scanner, list);

    }

    // =======================================================

    public void run(Scanner input, ArrayList<String> list) {

        double percentageC = getConfessions(list)/list.size();
        double percentageS = getSilent(list)/list.size();

        System.out.println(percentageS);
        

        Iterator<String> it = list.iterator();

        
        inputReader(input);

        if(percentageC > 0.3)
        {
            alwaysConfess(input);
        }
        else
        {
            alwaysSilent(input);
        }

    }

    public void alwaysConfess(Scanner input) 
    {
        System.out.println("Confess");
    }

    public void alwaysSilent(Scanner input)
    {
        System.out.println("Silent");
    }

    // =============================================================================================
    // tools

    public double getSilent(ArrayList methodArray) {

        double total = 0;

        for (int i = 0; i < methodArray.size(); i++) {
            if (methodArray.get(i).equals("silent")) {
                total++;

            }
        }

        return total;
    }

    public double getConfessions(ArrayList methodArray) {

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
    public void inputReader(Scanner x) {

        try {

            BufferedWriter file = new BufferedWriter(new FileWriter("Enemy_Input.txt", true));
            file.write(x.nextLine());
            file.newLine();
            file.close();

        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }

    }

}
