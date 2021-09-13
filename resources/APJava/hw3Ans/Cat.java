package src.hw3;

public class Cat {

    // 2 Shared fields that all other classes have
    private String name;
    private int age;

    // 1 unique field to the class
    private double knockRate;

    public Cat(String name, int age, double knockRate)
    {
        this.name = name;
        this.age = age;
        this.knockRate = knockRate;
    }

    /**
     * speak()
     * 
     * Generic speak method for speaking on its own
     */
    public void speak()
    {
        System.out.println(this.name + " the cat says Meowwwwww");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to other cats
     * @param c
     */
    public void speak(Cat c)
    {
        System.out.println(this.name + " the cat says Meowwwwww to " + c.getName() + " the cat.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to birds
     * @param b
     */
    public void speak(Bird b)
    {
        System.out.println(this.name + " the cat says Meowwwwww to " + b.getName() + " the bird.");
    }

    /**
     * speak()
     * 
     * Speak method for speaking to dolphins
     * @param d
     */
    public void speak(Dolphin d)
    {
        System.out.println(this.name + " the cat says Meowwwwww to " + d.getName() + " the dolphin.");
    }

    public double getKnockRate()
    {
        return this.knockRate;
    }

    public String getName()
    {
        return this.name;
    }

    public int getAge()
    {
        return this.age;
    }

    public void setKnockRate(double newRate)
    {
        this.knockRate = newRate;
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
