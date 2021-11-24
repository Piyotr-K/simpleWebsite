package backpack;

import java.util.ArrayList;
import java.util.Scanner;

/**
 * Simple little backpack program
 * Add stuff, remove stuff and list all stuff in side the backpack.
 */
public class backpack {
    
    public static void main(String[] args)
    {
        // Our backpack
        ArrayList<String> backpack = new ArrayList<String>();

        // Scanner for user input
        Scanner s = new Scanner(System.in);
        String userInput;

        p("You have opened your backpack.");
        p("What would you like to do?");
        p("1. Add Stuff\n2. Remove Something\n3. Show all items");
        userInput = s.nextLine();

        if (userInput.equals("1"))
        {
            p("adding");
            p("Enter an item to put in the backpack");
            userInput = s.nextLine();
            backpack.add(userInput);
        }
        else if (userInput.equals("2"))
        {
            p("Removing");
            // backpack.remove(?????????????);
        }
        else if (userInput.equals("3"))
        {
            p("Showing all items");
            p(backpack.toString());
        }

        s.close();
    }

    public static void p(String s)
    {
        System.out.println(s);
    }

    public static void add()
    {
    }

    public static void remove()
    {
    }

    public static void display()
    {
    }
}
