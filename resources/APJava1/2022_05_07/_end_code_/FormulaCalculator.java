import java.util.Scanner;
/**
 * FormulaCalculator.java
 * 
 * Lets the user choose whatever formula they want
 * and outputs their answer
 */
public class FormulaCalculator {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        // Math.PI or 3.14

        int tmp = 0;
        while(tmp != 3)
        {
            System.out.println("Welcome to the Formula Calculator");
            System.out.println("Please choose an option:");
            System.out.println("1. Surface Area of Cylinder");
            System.out.println("2. Volume of Cylinder");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            tmp = scan.nextInt();

            if (tmp == 1)
            {
                System.out.println("Please enter a height: ");
                double h = scan.nextDouble();
                System.out.println("Please enter a radius: ");
                double r = scan.nextDouble();
                double result = surfaceAreaCylinder(h, r);
                System.out.println("Your answer is " + result);
            }
        }

        System.out.println("Bye!");
    }

    public static double surfaceAreaCylinder(double height, double radius)
    {
        double part1 = 2 * Math.PI * radius * height;
        double part2 = 2 * Math.PI * radius * radius;
        return part1 + part2;
    }

    // Hmwk:
    // Required:
    // Finished Volume of Cylinder
    // Add surface area of sphere as choice 3
    // Add volume of sphere as choice 4
    // 
    // Challenge:
    // Find a way to shorten the amount of code in the main
    // The less the amount of code in main the better
}
