public class Class3 {

    static String name = "whoa";
    
    public static void main(String[] args) {
        // System.out.println(3 + 5 < 6 - 1);
        // whoa(1);
        random(3);
    }

    // Precondition: i > 1
    // Postcondition:
    public static void whoa(int i)
    {
        if (5 / (1 - i) > 0)
            return;
        // System.out.println(1 / 0);
    }

    public static void createCoffee()
    {
        System.out.println("Here is your coffee");
    }

    public static void createCoffee(int milkAmt, int creamAmt, int sugarAmt, boolean cup, String orderName)
    {
        System.out.println("Here is a coffee with " + milkAmt + " spoonfuls of milk");
        System.out.println("and " + creamAmt + " spoonfuls of cream");
        System.out.println("and " + sugarAmt + " spoonfuls of sugar.");
        if (cup)
            System.out.print("In a cup ");
        else
            System.out.print("In a glass ");
        System.out.print("for " + orderName);
    }

    public static void createCoffee(boolean cup, String orderName)
    {
        System.out.println("Here is a coffee.");
        if (cup)
            System.out.print("In a cup ");
        else
            System.out.print("In a glass ");
        System.out.print("for " + orderName);
    }

    public static void random(String num)
    {
        System.out.println(num);
    }

    public static void random(int number)
    {
        System.out.println(number);
    }
}
