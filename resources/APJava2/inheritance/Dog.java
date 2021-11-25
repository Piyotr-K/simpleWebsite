public class Dog extends Animal {
    private double runSpeed;

    public Dog(String name, int age, int runSpeed)
    {
        super(name, age);
        this.runSpeed = runSpeed;
        // System.out.println("Dog Constructor Called");
    }

    public Dog() { super("", 0); }

    public double getRunSpeed()
    {
        return runSpeed;
    }

    public void normalSpeak()
    {
        System.out.println("Ruff Ruff");
    }

    public void magicSpeak()
    {
        normalSpeak();
        super.magicSpeak();
    }
}
