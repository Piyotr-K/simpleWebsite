package classesPt2;

public class Area {
    
    // Instance/member method
    public double areaOfCircle(double radius)
    {
        return Math.PI * radius * radius;
    }

    // Class/static method
    public static double areOfTriangle(double base, double height)
    {
        return base * height / 2;
    }

    // Class/static method
    public static double areaOfSquare(double length, double width)
    {
        return length * width;
    }
}
