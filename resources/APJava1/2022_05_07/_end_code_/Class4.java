// import java.util.ArrayList;

public class Class4 {
    
    public static void main(String[] args) {
        // array vs a collection

        // array
        int[] listNumbers = new int[5]; // initialized to all zeroes
        int[] numbers;
        int[] nums = {100, 2, 23, 4, 5, 6, 0, 8, 9}; // initialize with default numbers

        // set values
        listNumbers[0] = 100;

        numbers = new int[10];

        // print an array like so:
        // for (int i = 0; i < listNumbers.length; i++)
        //     System.out.println(listNumbers[i]);
        
        // Enhanced for-loops do not allow you to modify
        // the array contents
        // sort-of read only
        // for (int i : listNumbers)
        //     i += 10;

        // "Normal" for-loops give you more control
        // Allowing you to modify array contents
        // for (int i = 0; i < listNumbers.length; i++)
        //     listNumbers[i] += 10;
        // printArr(numbers);

        // Create a function to double all numbers in a given int array
        // Just print, do not return

        // Create two functions to find the highest and lowest numbers in the given int array
        // and return the index of that number

        // print(func())
        System.out.println(maxNum(nums));
        System.out.println(minNum(nums));

        // Required:
        // A new function called sum
        // -> Sums up all the elements of a given array
        // A new function called specialSum
        // -> Sums up all the elements of a given array
        // -> If the difference between the largest number and the smallest num
        //    is greater than the largest num then multiply the sum by 2
        // A new function called order
        // -> If the largest number is after the smallest number return true
        // -> If the smallest number is after the largest number return false
        //
        // Challenge:
        // Have the user enter the array
        // Ask the user for a lenght first
        // Then ask the user for numbers to populate the array
    }

    public static void printArr(int[] a)
    {
        for (int n : a) System.out.println(n);
    }

    public static void doubleNums(int[] a)
    {
        for (int n : a) System.out.println(n * 2);
    }

    public static int maxNum(int[] a)
    {
        int max = a[0];
        int index = 0;

        for (int i = 0; i < a.length; i++)
        {
            if (a[i] > max)
            {
                max = a[i];
                index = i;
            }
        }

        return index;
    }

    public static int minNum(int[] a)
    {
        int min = a[0];
        int index = 0;

        for (int i = 0; i < a.length; i++)
        {
            if (a[i] < min)
            {
                min = a[i];
                index = i;
            }
        }

        return index;
    }
}
