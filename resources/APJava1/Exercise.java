package TwoDimensional;

public class Exercise {
    
    public static void main(String[] args) {
        int[][] matrix1 = { {1, 2, 3, 4},
                            {5, 6, 7, 8},
                            {9, 10, 11, 12},
                            {13, 14, 15, 16} };
        // Before incrementing by 1
        print2d(matrix1);
        IncrementByOne(matrix1);
        // After incrementing by 1
        print2d(matrix1);
    }

    // Increment all the numbers in the matrix by 1
    // Remember arrays are pass by reference*
    public static void IncrementByOne(int[][] mat)
    {
        // For each row
        for (int row = 0; row < mat.length; row++)
            // For each col in that row
            for (int col = 0; col < mat[row].length; col++)
                mat[row][col]++;
    }

    // Return the number of even numbers in the matrix
    public static int CountEvens(int[][] mat)
    {
        return -1;
    }

    public static void printPerimeter(int[][] mat)
    {
        // To-Do
        // Should print the perimeter of the mat
        // 1  2  3  4
        // 5        8
        // 9        12
        // 13 14 15 16
        return;
    }

    public static void printDiagonal(int[][] mat)
    {
        // To-Do
        // Should print this specific diagonal
        // 1
        //   6
        //     11
        //        16
        return;
    }

    // Prints 2d Array
    public static void print2d(int[][] mat)
    {
        for (int[] row : mat)
        {
            for (int col : row)
                System.out.print(col + "\t");
            System.out.println();
        }
    }
}
