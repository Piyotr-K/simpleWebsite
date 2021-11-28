package algorithms;

public class Recursion {

    public static void main(String[] args) {
        // recurse();
        // recurseUntil(10);
        // recurseUpTo(10);
        // recursionTime(0, 10);
        System.out.println(fibonacci(10));
    }

    public static void recurse()
    {
        System.out.println("Recursion time!!!!");
        recurse();
    }

    public static int recurseUntil(int num)
    {
        if (num == 0) return num;
        System.out.println("Recursion Number: " + num);
        return recurseUntil(num - 1);
    }

    public static int recursionTime(int start, int end)
    {
        if (start == end) return start;
        System.out.println("Recursion " + start);
        return recursionTime(start + 1, end);
    }

    public static int recurseUpTo(int num)
    {
        if (num == 0) return num;
        int tmp = recurseUpTo(num - 1);
        System.out.println("Recursion Number: " + tmp);
        return tmp;
    }

    public static int fibonacci(int n)
    {
        if (n == 0)
            return n;
        else if (n == 1)
            return n;
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}
