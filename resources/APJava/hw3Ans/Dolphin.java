package src.hw3;

public class Dolphin {

    // 2 Shared fields that all other classes have
    private String name;
    private int age;

    // 1 unique field to the class
    private double maxDepth;

    public Dolphin(String name, int age, double maxDepth)
    {
        this.name = name;
        this.age = age;
        this.maxDepth = maxDepth;
    }

    /**
     * speak()
     * 
     * Generic speak method for speaking on its own
     */
    public void speak()
    {
        System.out.println(this.name + " the dolphin says Echoooo");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to cats
     * @param c
     */
    public void speak(Cat c)
    {
        System.out.println(this.name + " the dolphin says Echoooo " + c.getName() + " the cat.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to birds
     * @param b
     */
    public void speak(Bird b)
    {
        System.out.println(this.name + " the dolphin says Echoooo to " + b.getName() + " the bird.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to other dolphins
     * @param d
     */
    public void speak(Dolphin d)
    {
        System.out.println(this.name + " the dolphin says Echoooo to " + d.getName() + " the dolphin.");
    }

    public double getMaxDepth()
    {
        return this.maxDepth;
    }

    public String getName()
    {
        return this.name;
    }

    public int getAge()
    {
        return this.age;
    }

    public void setMaxDepth(double newDepth)
    {
        this.maxDepth = newDepth;
    }

    public void setName(String newName)
    {
        this.name = newName;
    }

    public void setAge(int newAge)
    {
        this.age = newAge;
    }
}
