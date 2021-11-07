package Methods;

public class driver {

    public static void main(String[] args)
    {
        System.out.println("Driver");
        int[] arr1 = {1, 2, 3, 4, 5};
        System.out.println(arr1);
        printArr(reverser(arr1));
    }

    public static int[] reverser(int[] a)
    {
        int[] out = new int[a.length];
        int j = 0;
        for (int i = a.length - 1; i >= 0; i--)
        {
            out[j] = a[i];
            j++;
        }
        return out;
    }

    public static void printArr(int[] a)
    {
        for(int num : a)
            System.out.print(num + " ");
    }
}
