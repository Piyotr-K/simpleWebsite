public class Methods {
    
    public static void main(String[] args)
    {
        // Different ways to make an array
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = new int[5];

        arr2[0] = 5;
        for (int i = 0; i < arr1.length; i++)
            System.out.println(arr1[i]);

        // greet("Sam");
        // System.out.println(power(2, 3));
        // System.out.println(tellMeEven(6));
        // System.out.println(tellMeEven(5));
        // System.out.println(5 + 3 < 6 - 1);
    }

    public static void greet(String name)
    {
        System.out.println("Hello " + name);
        return; // void methods can still use the word return, just can\'t return anything
    }

    public static int power(int base, int exp)
    {
        int tmp = base;
        for (int i = 1; i < exp; i++)
        {
            base *= tmp;
        }
        return base;
    }

    public static int giveMeDaDouble(int num)
    {
        return num * 2;
    }

    // method signature: tellMeEven(int num)
    // Return true if the num is an even number
    // Return false if not
    // 3 % 2 = 1
    // 5 % 2 = 1
    // 6 % 2 = 0
    public static boolean tellMeEven(int num)
    {
        return num % 2 == 0;
    }
}
