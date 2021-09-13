public class Bird extends Animal {
    private double maxFlightHeight;

    public Bird(String name, int age, double maxFlightHeight)
    {
        super(name, age);
        this.maxFlightHeight = maxFlightHeight;
    }

    public double getMaxFlightHeight()
    {
        return maxFlightHeight;
    }

    public void normalSpeak()
    {
        System.out.println("tweet tweet");
        System.out.println("Chirp Chirp");
        System.out.println("Caw Caw");
    }

    public void magicSpeak()
    {
        normalSpeak();
        super.magicSpeak();
    }
}
