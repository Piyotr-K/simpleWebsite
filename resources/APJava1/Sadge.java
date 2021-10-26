import java.util.Scanner;

public class Sadge {
    
    public static void main(String[] args)
    {
        int ans = countDiv(20, 5);

        System.out.println(ans);

        String nice = "Nice shoes dude!";
        nice.charAt(0); // N
        nice.charAt(5); // s
        nice.substring(0, 3); // Nic
        System.out.println(nice.substring(5)); // shoes dude!
        System.out.println(nice.substring(2, 8)); // ce sho
    }

    public static int countDiv(int num, int divisor)
    {
        // count the number of times that you need to divide num by 2
        // before you get 1
        // use a while loop
        // return number of 2 divisions
        // 20 / 2 = 10 / 2 = 5 / 2 = 2 / 2 = 1
        // countDiv(20, 5) -> 2
        int counter = 0;
        while (num >= 2) {
            num /= divisor;
            counter++;
        }
        return counter;
    }

    public static void whileExample()
    {
        // Make a new Scanner object
        Scanner in = new Scanner(System.in);
        boolean done = false;
        String output = "";
        while (!done)
        {
            System.out.println("Enter a number, press 'q' to stop:");
            // Everytime you need to use scanner, you have to call the nextLine() function
            String tmp = in.nextLine();

            if (tmp.equals("q"))
            {
                output = output.substring(0, output.length() - 2);
                done = true;
            }
            else
            {
                output += tmp + ", ";
            }
        }
        System.out.println(output);
    }
}
