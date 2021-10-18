package src.ArraysExamples;

public class examples {

    public static void main(String[] args)
    {
        stuff();
    }

    public static void printArr(int[] arr)
    {
        for (int i = 0; i < arr.length; i++)
        {
            System.out.print(arr[i] + ",");
        }
        System.out.println();
    }

    public static void stuff()
    {
        int[] arr1 = {1, 2, 3, 4, 5};
        int[] tmp = new int[arr1.length * 2];

        System.out.println("Array 1 before expand");
        printArr(arr1);

        for (int i = 0; i < arr1.length; i++)
        {
            tmp[i] = arr1[i];
        }

        arr1 = tmp;
        System.out.println("Array 1 after expand");
        printArr(arr1);

        arr1[5] = 6;
        arr1[6] = 7;
        System.out.println("Array 1 after expand and add moar");
        printArr(arr1);
        System.out.println(arr1.length);
    }
}