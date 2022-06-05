import java.util.Scanner;

public class Class5 {
    
    public static void main(String[] args) {
        String s = "hello world lol haha";

        inClassThing();

        // If given 2 parameters, start at the first index and go until but NOT including
        // the ending index
        // System.out.println(s.substring(0, 4)); -> hell
        // System.out.println(s.substring(0, s.length())); -> hello world (does not crash)
        // System.out.println(s.substring(0, s.length()) + 1); -> IndexOutOfBoundsException

        // If given 1 parameter, start at the index given and go until the end of the string
        // System.out.println(s.substring(5));

        // charAt() NOT on exam anymore, returns a char type
        // System.out.println(s.charAt(0)); // -> 109???!??!
        // System.out.println(s.substring(0, 1) + 5); // -> h5

        // Lazy copy
        // String s2 = "lol";
        // String s3 = "lol";
        // Hashcode stuff
        // String s2 = "lol";
        // String s3 = new String("lol");

        // System.out.println(s2 == s3);

        // IndexOf
        // System.out.println(s.indexOf("hell")); -> return 0
        // System.out.println(s.indexOf("hellx")); -> return -1, because does not exist
        // System.out.println(s.indexOf(" lo")); -> returns 11, because there

        // CompareTo - Lexicographically (dictionary order "ASCII order")
        // a < z
        // q > e
        // tip: always check which string is on the left, that way you know
        // whether it will be negative or not
        // String s2 = "*";
        // System.out.println(s2.compareTo("z"));
        
        // String j = removeSpaces(s);
        // System.out.println(j);
    }

    public static void inClassThing()
    {
        // First number (n) is the number of words the user will enter
        // The next n Strings will be the words
        // Output all the strings the user entered in dictionary order
        //
        // Sample Input:
        // 5
        // Lol
        // ABdddd
        // Deeeee
        // JJJJJJj
        // Lel
        // 
        // Sample Output:
        // ABdddd
        // Deeeee
        // JJJJJJj
        // Lel
        // Lol
        // 
        // Hint: use String array -> String[] words = new String[size];
        Scanner scan = new Scanner(System.in);
        String[] words;
        int size;
        System.out.print("Enter number of words: ");
        size = scan.nextInt();
        words = new String[size];
        System.out.println("Enter words:");

        for(int i = 0; i < size; i++)
            words[i] = scan.next();

        // for (int i = 0; i < words.length - 1; i++)
        // {
        //     if (words[i].compareTo(words[i+1]) < 0)
        //     {
        //     }
        // }

    }

    public static void stringTraversal(String s)
    {
        for (int i = 0; i < s.length(); i++)
            System.out.println(s.substring(i, i + 1));
    }

    public static String removeSpaces(String s)
    {
        String out = "";
        for (int i = 0; i < s.length(); i++)
        {
            String buf = s.substring(i, i + 1);
            if (!buf.equals(" "))
                out += buf;
        }
        return out;
    }
}