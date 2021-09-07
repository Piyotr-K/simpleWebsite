package classesPt2;

public class driver {

    public static void foo(int x, double y)
    {
        x = 3;
        y = 2.5;
    }
    
    public static void main(String[] args)
    {
        Area area1 = new Area();
        System.out.println("Area of a square " + Area.areaOfSquare(5, 5));
        System.out.println("Area of a circle " + area1.areaOfCircle(2.5));

        int a = 7;
        double b = 6.5;
        foo(a, b);
        System.out.println(a + " " + b);
    }
}
