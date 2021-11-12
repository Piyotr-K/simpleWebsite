package Caesar;

import java.util.Scanner;
import java.util.ArrayList;

public class caesar {

    public static void main(String[] args) {
        char[] alphabet = {'a', 'b', 'c', 'd', 'e', 'f',
                            'g', 'h', 'i', 'j', 'k', 'l',
                            'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x',
                            'y', 'z'};
        ArrayList<Character> alphabet2 = new ArrayList<Character>();

        // Add all characters from alphabet to the new "better" alphabet2
        for (char c : alphabet)
            alphabet2.add(c);

        int key = 0; //, pos = 0, finalPos = 0;
        String userInput, userKey, encrypted = "";
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a message: ");
        userInput = input.nextLine(); // Get the user's input as a String

        System.out.print("Enter a key to use: ");
        userKey = input.nextLine();
        key = Integer.parseInt(userKey); // Convert the user's input into a integer

        encrypted = encryptMsg(key, userInput, alphabet2);

        System.out.println("Original Message:");
        System.out.println(userInput);
        System.out.println("Encrypted Message:");
        System.out.println(encrypted);

        input.close();
    }

    public static void listStuff()
    {
        ArrayList<Integer> list1 = new ArrayList<Integer>();
        list1.add(5);
        list1.add(9);
        list1.add(10);
        System.out.println(list1);
        int pos = list1.indexOf(10); // get the position of the item
        System.out.println(pos);
        System.out.println(list1.get(0)); // list1[0] -> returns the first item
    }

    // Create a new function that returns the encrypted string
    // Takes a string to be encrypted and an int for the key you're using
    // Also takes an ArrayList of alphabet letters to choose from
    // Out -> encrypted string (type: String)
    // In -> int key, String msg, ArrayList alph
    public static String encryptMsg(int key, String msg, ArrayList<Character> alph)
    {
        int pos = 0, finalPos = 0;
        String encrypted = "";
        for (int i = 0; i < msg.length(); i++)
        {
            // To find the position of the user's entered character
            pos = alph.indexOf(msg.charAt(i));
            finalPos = (pos + key) % 26;
            encrypted += alph.get(finalPos);
        }

        return encrypted;
    }
}
