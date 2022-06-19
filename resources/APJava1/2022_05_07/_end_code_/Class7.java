public class Class7 {
    public static void main(String[] args) {
        System.out.println(pow(10));

        // Make a power of 2 function
        // Must use recursion
        // Don't use print in the function
        // So if I did pow(10) -> 1024
        // pow(2) -> 4

        // Coding bat recursion
        // Hw:
        // bunnyEars2, triangle, sumDigits
        // Spicy:
        // count7, count8, powerN
    }

    public static void example1()
    {
        // This causes a stackoverflow
        // Goes on forever

        System.out.println("Hi");
        example1();
    }

    public static void example2(int i)
    {
        if (i == 0) // End condition
            return; // Stopping point
        
        // How do we get to the ending condition?
        // We want to get to 0, so we subtract
        example2(i - 1);
        System.out.println(i);

        // ex2(10) -> ex2(9) -> ex2(8) ... ex2(0)
    }

    public static int example3(int i)
    {
        if (i == 0)
            return 0;
        return i + example3(i - 1);
        // ex(10) -> ... ex(0)
    }

    public static int pow(int i)
    {
        if (i == 0) return 1;
        return 2 * pow(i - 1);
    }
}
