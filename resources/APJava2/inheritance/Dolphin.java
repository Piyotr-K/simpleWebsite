public class Dolphin extends Animal {
    private double swimDepth;

    // Sub-class constructor
    public Dolphin(String name, int age, double swimDepth)
    {
        super(name, age);
        this.swimDepth = swimDepth;
    }

    public double getSwimDepth()
    {
        return swimDepth;
    }

    public void normalSpeak()
    {
        System.out.println("echo echo echo");
    }

    public void magicSpeak()
    {
        normalSpeak();
        super.magicSpeak();
    }
}
