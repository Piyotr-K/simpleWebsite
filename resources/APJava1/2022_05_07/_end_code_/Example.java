import java.util.Scanner;

public class Example
{
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);

        System.out.print("Enter something: ");
        String userInput = scan.nextLine();
        System.out.println("What you entered: " + userInput);
        System.out.print("Enter something: ");
        int hee = scan.nextInt();
        System.out.println("What you entered: " + hee);

        // Required:
        // Write a program that asks the user for their name, age
        // Print out "Hello " + whatever name
        // For age, print out "You can drive" if their age is over 16
        // If not print "You cannot drive"

        // int, boolean, double
        // short, long, float, char, byte

        // String random = "hello";
        // String test = "these two strings ";
        // String test2 = "\"will be o\\\n the same line!\"";
        // String otherStuff = "\t, \r, \b"; // no need to know, but cool
        // System.out.print(test);
        // System.out.println(test2);
        // test = "cool";
        // // System.out.print(test + test2); // called string concatenation
        // char a = 't';

        // A single line comment
        // Which means that this is a separate line

        /*
        This is a multi line comment
        Which means that we're good
        even if we're on
        separate lines
        as long as its before the ending symbol
        */

        // int x = (int) 5.1; // truncation is not the same as rounding
        // int y = (int) 5.9; // y = 5
        // System.out.println(y);
        // String random2 = "hello";

        // int x = 5, y = 8;
        // if (x > 5)
        //     if (y == 8)
        //     {
        //         x = 6;
        //         y = 9;
        //     }
        //     else
        //         x = 7;
        // else
        //     y = 10;

        // // What is the value of x and y after this is run
        // System.out.println("x is " + x + ", y is " + y);
    }
}