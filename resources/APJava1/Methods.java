public class Methods {
    
    public static void main(String[] args)
    {
        // Different ways to make an array
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] arr2 = new int[5];

        int[] exercise1 = {1, 2, 3, 4, 5, 6};
        int[] exercise2 = {1, 2, 3, 4, 5, 6, 7};

        // Array are poopy but they take up less memory and do simple
        // Lists are better but take up moar memory and do big complex

        // given an array see if there is a negative number in it
        // if there is return true otherwise false
        // make a new function
        // use a for loop
        System.out.println(arrNegative(exercise1));

        // given an array find if the sum is an even or odd number
        // if it is even return true, if odd return false;
        System.out.println(arrSumEven(exercise2));

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

    public static void question1()
    {
        int num = 22;
        if (num > 0)
        if (num % 5 == 0)
        System.out.println(num);
        else System.out.println(num + " is negative");
    }

    public static void question2()
    {
        int x = 30, y = 40;
        if (x >= 0)
        {
            if (x <= 100)
            {
                y = x * 3;
                if (y < 50)
                    x /= 10;
            }
            else
                y = x * 2;
        }
        else
            y = -x;
        System.out.println("x: " + x + ", y: " + y);
    }

    public static void question3()
    {
        int a = 5, b = 4, n = 6;
        // a != b
        if (a != b && n / (a-b) > 90)
        {
            /* statement 1 */
        }
        else
        {
            /* statement 2 */
        }
        /* statement 3 */

        // A) statement 1 will be exectued
        // B) statement 2 will be executed
        // C) either statement 1 or statement 2
        // D) Compile die
        // E) Exception -> "Crash"
    }

    public static boolean arrNegative(int[] arr)
    {
        for (int i = 0; i < arr.length; i++)
        {
            if (arr[i] < 0)
                return true;
        }
        return false;
    }

    public static boolean arrSumEven(int[] arr)
    {
        int sum = 0;
        for (int i = 0; i < arr.length; i++)
        {
            sum += arr[i];
        }
        return sum % 2 == 0;
    }
}
